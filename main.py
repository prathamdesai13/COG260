from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *

import numpy as np

fociDictionary = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':

    # pmap = prob_map(namingData, 1)
    # cmap = consolidate_map(pmap)
    # print(cmap)
    
    # print(universal_terms(namingData, 1))
    # print(universal_terms(fociDictionary, 1))
    
    pmap = prob_map(namingData, 1)
    cmap = consolidate_map(pmap)
    print(cmap)