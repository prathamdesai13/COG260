import numpy as np
import scipy as sp
from random import shuffle

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
        cmap[cell] = {max_colours[0] : max_votes}
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

    return sp.spatial.distance.euclidean(x, y)
    

def similarity_func(x, y):

    return np.exp(-np.power(euclidean_dist(x, y), 2.0))

# all cells exemplar prediction function
# uses a similarity function to categorize new data points
def all_cells_exemplar_predict(cmap):

    pass


def assign_colour(cell, prototypes):

    min_dist = 10000000 # some very big distance
    best_fit_colour = None
    for term in prototypes.keys():
        dist = euclidean_dist(cell, prototypes[term])
        if min_dist > dist:
            min_dist = dist
            best_fit_colour = term
    return best_fit_colour

def prototype_predict(prototypes):
    """
    Prototypes is a dictionary of key = colour label, and value = cell
    Iterate through a blank map of cells, assign each cell a colour
    based on distance from prototype cells
    """
    num_cells = 330
    out_map = [None for _ in range(num_cells)]
    for cell in range(num_cells):
        out_map[cell] = assign_colour(cell, prototypes)
    return out_map