import numpy as np

# generates majority colour map for a specified language
# cmap should be randomized on ties
def consolidate_map(pmap):
    cmap = {}
    for cell in pmap.keys():
        max_colour = None
        max_votes = -1
        for colour in pmap[cell]:
            num_vote = pmap[cell][colour]
            if num_vote > max_votes:
                max_colour = colour
                max_votes = num_vote
        cmap[cell] = {max_colour : max_votes}
    return cmap

# prototype model stuff
def universal_terms(data, language):
    """
    Generates a list of colour terms used by any of the speakers of a given language
    """
    universal_terms = set()
    for speaker in fociDictionary[data][language]:
        for term in fociDictionary[data][language][speaker]:
            universal_terms.add(term)
    return list(universal_terms)

# calculates the euclidean distance between two vectors
def euclidean_dist(x, y):

    return np.linalg.norm(x, y)
    

def similarity_func(x, y):

    return np.exp(-euclidean_dist(x, y))

# all cells exemplar prediction function
# uses a similarity function to categorize new data points
def all_cells_exemplar_predict(cmap):




def prototype_predict(cmap):
    """
    
    """
    terms = universal_terms(language)