# probability map
# generates a superimposed map of all the colour maps elicited from speakers of a language,
# for evaluation of prediction models

from PrathUnits import universal_terms
from wcs_helper_functions import readChipData, readClabData,  readFociData
import string

cnumDictionary, cnameDictionary = readChipData('./WCS_data_core/chip.txt')
clabDictionary = readClabData('./WCS_data_core/cnum-vhcm-lab-new.txt')
foci_data = readFociData('./WCS_data_core/foci-exp.txt')

def prob_map(data, language):
    count_map = {}
    prob_map = {}
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
                    
    for cell in count_map:
        total = sum(list(count_map[cell].values()))
        prob_map[cell] = {colour: (count_map[cell][colour]) / total for colour in count_map[cell]}
    return prob_map

# returns score of how well the prediction_map matches the prob_map
def evaluate(prediction_map, prob_map):
    score = 0
    num_cells = len(prediction_map)
    for cell in range(1, 331):
        prediction = prediction_map[cell]
        if prediction in prob_map[cell]:
            score += prob_map[cell][prediction]
    return score / 330
 
def make_foci_exemplars(data, language):            # FOCI EXEMPLARS
    terms = universal_terms(data, language)
    foci_exemplars = {term: [] for term in terms}
    for speaker in data[language]:
        for term in terms:
            if term in data[language][speaker]:
                for cell in data[language][speaker][term]:
                    foci_exemplars[term].append(float_tuple(clabDictionary[cnumDictionary[cell.replace(":", "")]]))
    return foci_exemplars

def make_foci_prototypes(data, language):           # FOCI PROTOTYPES
    foci_exemplars = make_foci_exemplars(data, language)
    foci_prototypes = {}
    for term in foci_exemplars:
        foci_prototypes[term] = tuple_average(foci_exemplars[term])
    return foci_prototypes

def tuple_average(tuple_list):
    num_tup = float(len(tuple_list))
    tup_length = len(tuple_list[0])
    return tuple(sum(n[i] for n in tuple_list)/num_tup for i in range(tup_length))

def float_tuple(string_tuple):
    n1, n2, n3 = string_tuple
    return (float(n1), float(n2), float(n3))
    

if __name__ == "__main__":
    # print(clabDictionary["D9"])
    
    LANGUAGE = 3
    
    exemplars = make_foci_exemplars(foci_data, LANGUAGE)
    print(exemplars)
    prototypes = make_foci_prototypes(foci_data, LANGUAGE)
    print(prototypes)