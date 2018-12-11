from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *

import numpy as np

foci_data = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':
    ACE_performances = []
    FE_performances = []
    FP_performances = []
    
    for LANGUAGE in range(1, 111):
        print(f"Language {LANGUAGE}:")
        pmap = prob_map(namingData, LANGUAGE)
        cmap = consolidate_map(pmap)
        
        # BASELINE
        baseline = evaluate(cmap, pmap)
        print(f"{baseline} - BASELINE")
        
        # ALL CELLS EXEMPLAR
        ACE = evaluate(all_cells_exemplar_predict(cmap), pmap)
        print(f"{ACE} - ALL-CELLS EXEMPLAR")
        ACE_performances.append(ACE / baseline)
        
        # FOCI EXEMPLAR
        foci_exemplars = make_foci_exemplars(foci_data, LANGUAGE)
        FE = evaluate(foci_exemplar_predict(foci_exemplars), pmap)
        print(f"{FE} - FOCI EXEMPLAR")
        FE_performances.append(FE / baseline)
        
        # FOCI PROTOTYPE
        foci_prototypes = make_foci_prototypes(foci_exemplars)
        FP = evaluate(foci_prototype_predict(foci_prototypes), pmap)
        print(f"{FP} - FOCI PROTOTYPE")
        FP_performances.append(FP / baseline)
    
    print("{np.mean(ACE_performances)} - PERFORMANCE OF ALL CELLS EXEMPLAR")
    print("{np.mean(FE_performances)} - PERFORMANCE OF FOCI EXEMPLAR")
    print("{np.mean(FP_performances)} - PERFORMANCE OF FOCI PROTOTYPE")
    