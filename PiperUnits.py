# probability map
# generates a superimposed map of all the colour maps elicited from speakers of a language,
# for evaluation of prediction models

from PrathUnits import universal_terms
from wcs_helper_functions import readChipData, readClabData

cnumDictionary, cnameDictionary = wcs.readChipData('./WCS_data_core/chip.txt')
clabDictionary = readClabData('./WCS_data_core/cnum-vhcm-lab-new.txt')

LANGUAGE = 1

def prob_map(data, language):
    """
    Constructs language map for each participant which
    """
    count_map = {}
    for speaker in data[language]:
        for cell in data[language][speaker]:
            colour = data[language][speaker][cell]
            if cell not in count_map:
                count_map[cell] = {colour: 1}
            else:
                if colour not in count_map[cell]:
                    count_map[cell][colour] = 1
                else:
                    count_map[cell][colour] += 1
    return count_map

# returns score of how well the prediction_map matches the prob_map
def score(prob_map, prediction_map):
    score = 0
    num_cells = len(prediction_map)
    for cell in range(num_cells):
        if prediction_map[cell] in prob_map[cell]:
            score += prob_map[prediction_map[cell]]
 
def make_foci_exemplars(data, language):
    terms = universal_terms(data, language)
    foci_exemplars = {term: [] for term in terms}
    for speaker in data[language]:
        for term in terms:
            if term in data[language][speaker]:
                foci_exemplars[term] += data[language][speaker][term]
    return foci_exemplars

def make_foci_prototypes(data, language):
    all_foci = make_foci_exemplars(data, language)
    cielab_foci = {term: [] for term in all_foci}
    for term in all_foci:
        foci = all_foci[term]
        for focus in foci:
            cielab_foci[term].append(clabDictionary[cnumDictionary[term]])

def tuple_average(tuple_list):
    num_tup = float(len(tuple_list))
    tup_length = len(tuple_list[0])
    return tuple(sum(n[i] for n in tuple_list)/num_tup for i in range(tup_length))
    

if __name__ == "__main__":
    pass