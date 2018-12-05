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
        print(f"Language {LANGUAGE}:")
        print(f"Unique terms: {len(universal_terms(fociDictionary, LANGUAGE))}")
<<<<<<< Updated upstream
        print(f"{evaluate(cmap, pmap)} - BASELINE")
        print(f"{evaluate(all_cells_exemplar_predict(cmap), pmap)} - ALL-CELLS EXEMPLAR")
        # print(cmap)
        # print(all_cells_exemplar_predict(cmap))
=======
        # print(f"{evaluate(cmap, pmap)} - BASELINE")
        # print(f"{evaluate(all_cells_exemplar_predict(cmap), pmap)} - ALL-CELLS EXEMPLAR)
        print(cmap)
        print(all_cells_exemplar_predict(cmap, LANGUAGE))
>>>>>>> Stashed changes
        print()