from wcs_helper_functions import *

import numpy as np

import matplotlib.pyplot as plt

fociDictionary = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

# probability map
# generates a superimposed map of all the colour maps elicited from speakers of a language, 
# for evaluation of prediction models

LANGUAGE = 1

def prob_map(language):
    """
    Constructs language map for each participant which
    """
    count_map = {}
    for speaker in namingData[language]:
        for cell in namingData[language][speaker]:
            colour = namingData[language][speaker][cell]
            if cell not in count_map:
                count_map[cell] = {colour: 1}
            else:
                if colour not in count_map[cell]:
                    count_map[cell][colour] = 1
                else:
                    count_map[cell][colour] += 1
    return count_map

# print(prob_map(LANGUAGE))
pmap = prob_map(LANGUAGE)
print(pmap)


# generates majority colour map for a specified language
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
print(consolidate_map(pmap))
