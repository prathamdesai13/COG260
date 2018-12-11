from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *

import numpy as np

fociDictionary = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':
    performances = []
    for LANGUAGE in range(1, 111):
        pmap = prob_map(namingData, LANGUAGE)
        cmap = consolidate_map(pmap)
        # fex = make_foci_exemplars(fociDictionary, LANGUAGE)
        
        # print(f"Language {LANGUAGE}:")
        
        # print(f"Unique terms: {len(universal_terms(fociDictionary, LANGUAGE))}")
        baseline = evaluate(cmap, pmap)
        # print(f"{baseline} - BASELINE")
        ACE = evaluate(all_cells_exemplar_predict(cmap), pmap)
        # print(f"{ACE} - ALL-CELLS EXEMPLAR")
        performances.append(ACE / baseline)

        print(LANGUAGE)
    print("Average performance over all languages:")
    print(np.mean(performances))
    # foci_exemplars = make_foci_exemplars(fociDictionary, 1)
    # print(foci_exemplars)