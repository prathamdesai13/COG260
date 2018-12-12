from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *
from time import time
import numpy as np
import matplotlib.pyplot as plt
from data_analysis import *

foci_data = readFociData('./WCS_data_core/foci-exp.txt')
namingData = readNamingData('./WCS_data_core/term.txt')

if __name__ == '__main__':
    for language in [25, 35]:
        outputs = pipeline(namingData, foci_data, language)
        title1 = 'CMAP | Language ' + str(language)
        title2 = 'FE Prediction | Language ' + str(language)
        title3 = 'FP Prediction | Language ' + str(language)
        cmap_encoded = map_array_to(list(outputs['cmap'].values()), generate_random_values(list(outputs['cmap'].values())))
        FE_encoded = map_array_to(list(outputs['FE'].values()), generate_random_values(list(outputs['FE'].values())))
        FP_encoded = map_array_to(list(outputs['FP'].values()), generate_random_values(list(outputs['FP'].values())))
        plotValues(cmap_encoded, title1, seq=1)
        plotValues(FE_encoded, title2, seq=2)
        plotValues(FP_encoded, title3, seq=3)
        plt.show()
    
