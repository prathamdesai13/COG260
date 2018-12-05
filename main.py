from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *

import numpy as np

fociDictionary = readFociData('./WCS_data_core/foci-exp.txt')

namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':
    LANGUAGE = 2
    pmap = prob_map(namingData, LANGUAGE)
    print("pmap:\n" + str(pmap))
    cmap = consolidate_map(pmap)
    print()
    print("cmap:\n" + str(cmap))
    print(evaluate(cmap, pmap))