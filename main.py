from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *
from time import time
import numpy as np
import matplotlib.pyplot as plt

foci_data = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

def plot_accuracy_terms(performance, terms):
    
    pass

if __name__ == '__main__':
    start = time()
    ACE_performances = []
    FE_performances = []
    FP_performances = []
    FE_beats_FP = 0
    FP_beats_FE = 0
    
    for LANGUAGE in range(1, 111):
        print(f"--------------------- Language {LANGUAGE} ---------------------------")
        print()
        pmap = prob_map(namingData, LANGUAGE)
        cmap = consolidate_map(pmap)
        
        # BASELINE
        baseline = evaluate(cmap, pmap)
        print(f"{baseline} - BASELINE")
        print()
        
        # ALL CELLS EXEMPLAR
        ACE = evaluate(all_cells_exemplar_predict(cmap), pmap)
        print(f"{ACE} - ALL-CELLS EXEMPLAR")
        print()
        ACE_performances.append(ACE / baseline)
        
        # FOCI EXEMPLAR
        foci_exemplars = make_foci_exemplars(foci_data, LANGUAGE)
        FE = evaluate(foci_exemplar_predict(foci_exemplars), pmap)
        print(f"{FE} - FOCI EXEMPLAR")
        print()
        FE_performances.append(FE / baseline)
        
        # FOCI PROTOTYPE
        foci_prototypes = make_foci_prototypes(foci_exemplars)
        FP = evaluate(foci_prototype_predict(foci_prototypes), pmap)
        print(f"{FP} - FOCI PROTOTYPE")
        print()
        FP_performances.append(FP / baseline)
        
        if FE < FP:
            FE_beats_FP += 1
        elif FP < FE:
            FP_beats_FE += 1
    
    print(f"{np.mean(ACE_performances)} - PERFORMANCE OF ALL CELLS EXEMPLAR")
    print(f"{np.mean(FE_performances)} - PERFORMANCE OF FOCI EXEMPLAR")
    print(f"{np.mean(FP_performances)} - PERFORMANCE OF FOCI PROTOTYPE")
    print(f"Foci Exemplar beat Foci Prototype {FE_beats_FP} times")
    print(f"Foci Prototype beat Foci Exemplar {FP_beats_FE} times")
    
    end = time() 
    print(f"Program ran in {end - start}")
    
    