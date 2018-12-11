import numpy as np
import scipy.spatial as sp
from random import shuffle
from wcs_helper_functions import *

def load_munsell():

    return readChipData('./WCS_data_core/chip.txt')

# generates majority colour map for a specified language
# cmap should be randomized on ties
def consolidate_map(pmap):
    cmap = {}
    for cell in pmap.keys():
        max_votes = -1
        for colour in pmap[cell]:
            num_vote = pmap[cell][colour]
            if num_vote > max_votes:
                max_votes = num_vote
        max_colours = []
        for colour in pmap[cell]:
            if pmap[cell][colour] == max_votes:
                max_colours.append(colour)
        shuffle(max_colours) # shuffle colours to allow randomness in ties
        cmap[cell] = max_colours[0]
    return cmap

# prototype model stuff
def universal_terms(data, language):
    """
    Generates a list of colour terms used by any of the speakers of a given language and given dataset
    """
    universal_terms = set()
    for speaker in data[language]:
        for term in data[language][speaker]:
            universal_terms.add(term)
    return list(universal_terms)

# calculates the euclidean distance between two vectors
def euclidean_dist(x, y):

    return sp.distance.euclidean(x, y)
    

def similarity_func(x, y):

    return np.exp(-np.power(euclidean_dist(x, y), 2.0))

# all cells exemplar prediction function
# uses a similarity function to categorize new data points
def all_cells_exemplar_predict(cmap):
    num_cells = 330
    out_map = {i + 1 : None for i in range(num_cells)}
    sims = {}
    clabDictionary = readClabData('./WCS_data_core/cnum-vhcm-lab-new.txt')
    for cell in cmap.keys():
        colour_term = cmap[cell]
        if colour_term not in sims:
            sims[colour_term] = 0
    
    for cell in range(num_cells):
        (n1, n2, n3) = clabDictionary[cell + 1]
        clab_coord = (float(n1), float(n2), float(n3))
        for term in sims:
            for cell_i in cmap.keys():
                if term == cmap[cell_i] and cell_i != (cell + 1):
                    (n1, n2, n3) = clabDictionary[cell_i]
                    cell_i_coord = (float(n1), float(n2), float(n3))
                    sims[term] += similarity_func(clab_coord, cell_i_coord)
        max_key = max(sims, key=lambda k: sims[k])
        out_map[cell + 1] = max_key
        for keys in sims.keys():
            sims[keys] = 0
    return out_map

def assign_colour(cell_coord, prototypes, func):
    min_dist = 10000000 # some very big distance
    best_fit_colour = None
    for term in prototypes.keys():
        dist = func(cell_coord, prototypes[term])
        if min_dist > dist:
            min_dist = dist
            best_fit_colour = term
    return best_fit_colour

def corresponding_munsell(cell):
    """
    Cell is a value in [0, 330)
    """
    munsell_info = load_munsell()
    index_to_coord = munsell_info[1][cell + 1]
    return str(index_to_coord[0] + str(index_to_coord[1]))


def foci_prototype_predict(prototypes):
    """
    Prototypes is a dictionary of key = colour label, and value = cell
    Iterate through a blank map of cells, assign each cell a colour
    based on distance from prototype cells
    """
    num_cells = 330
    out_map = { i + 1 : None for i in range(num_cells)}
    clabDictionary = readClabData('./WCS_data_core/cnum-vhcm-lab-new.txt')
    for cell in range(num_cells):
        (n1, n2, n3) = clabDictionary[cell + 1]
        cell_coord = (float(n1), float(n2), float(n3))
        out_map[cell + 1] = assign_colour(cell_coord, prototypes, euclidean_dist)
    return out_map

def foci_exemplar_predict(exemplars):
    """
    exemplars: key=colour term , value=list of cells
    """

    num_cells = 330
    out_map = { i + 1 : None for i in range(num_cells)}
    clabDictionary = readClabData('./WCS_data_core/cnum-vhcm-lab-new.txt')
    sims = {}
    for colour_term in exemplars.keys():
        if colour_term not in sims:
            sims[colour_term] = 0

    for cell in range(num_cells):
        (n1, n2, n3) = clabDictionary[cell + 1]
        cell_coord = (float(n1), float(n2), float(n3))
        for term in sims:
            for foci_cell in exemplars[term]:
                (n1, n2, n3) = clabDictionary[foci_cell]
                foci_coord = (float(n1), float(n2), float(n3))
                sims[term] += similarity_func(cell_coord, foci_coord)
        max_key = max(sims, key=lambda k: sims[k]) # pick out the colour term with highest similarity
        out_map[cell + 1] = max_key
        for keys in sims.keys():
            sims[keys] = 0
    return out_map
