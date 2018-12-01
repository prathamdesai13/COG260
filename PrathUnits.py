# probability map
# generates a superimposed map of all the colour maps elicited from speakers of a language,
# for evaluation of prediction models

LANGUAGE = 1

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
def universal_terms(language):
    """
    Generates a list of colour terms used by any of the speakers of a given language
    """
    universal_terms = set()
    for speaker in fociDictionary[language]:
        for term in fociDictionary[language][speaker]:
            universal_terms.add(term)
    return list(universal_terms)


def prototype_predict(cmap):
    """
    
    """
    terms = universal_terms(language)