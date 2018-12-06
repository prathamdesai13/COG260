from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *

import numpy as np

fociDictionary = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':
    for LANGUAGE in range(1, 101):
        pmap = prob_map(namingData, LANGUAGE)
        cmap = consolidate_map(pmap)
        fex = make_foci_exemplars(fociDictionary, LANGUAGE)
        print(f"Language {LANGUAGE}:")
        
        print(f"Unique terms: {len(universal_terms(fociDictionary, LANGUAGE))}")
        
        print(f"{evaluate(cmap, pmap)} - BASELINE")
        
        print(f"{evaluate(all_cells_exemplar_predict(cmap), pmap)} - ALL-CELLS EXEMPLAR")
        
        print(f"{evaluate(foci_exemplar_predict(fex, pmap))} - FOCI EXEMPLAR")

        print()
    # foci_exemplars = make_foci_exemplars(fociDictionary, 1)
    # print(foci_exemplars)