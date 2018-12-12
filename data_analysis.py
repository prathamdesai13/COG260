from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *
from time import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

# generates slope and intercept for specified data
def line_of_best_fit(x, y):

    return np.polyfit(x, y, deg=1)

# sorts list based on specified indexes to sort
def sort_in_parallel(to_sort, indices):

    return [x for _, x in sorted(zip(indices, to_sort))]

# gets model scores over all languages
# mainly used to nicely display scores for each model for each language
def get_model_scores(namingData, foci_data):
    ACE_performances = []
    FE_performances = []
    FP_performances = []
    FE_beats_FP = 0
    FE_beats_FP_languages = []
    FP_beats_FE = 0
    FP_beats_FE_languages = []
    
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
            FE_beats_FP_languages.append(LANGUAGE)
        elif FP < FE:
            FP_beats_FE += 1
            FP_beats_FE_languages.append(LANGUAGE)

    print(f"{np.mean(ACE_performances)} - PERFORMANCE OF ALL CELLS EXEMPLAR")
    print(f"{np.mean(FE_performances)} - PERFORMANCE OF FOCI EXEMPLAR")
    print(f"{np.mean(FP_performances)} - PERFORMANCE OF FOCI PROTOTYPE")

    print(f"Foci Exemplar beat Foci Prototype {FE_beats_FP} times")
    print(f"Foci Prototype beat Foci Exemplar {FP_beats_FE} times")

    print("Languages that FE beat FP: ", FE_beats_FP_languages)
    print("Languages that FP beat FE: ", FP_beats_FE_languages)

# generate output maps for specified language
def pipeline(naming_data, foci_data, language):

    outputs = {}

    # generate probability map
    pmap = prob_map(naming_data, language)
    outputs['pmap'] = pmap

    # generate consolidated map
    cmap = consolidate_map(pmap)
    outputs['cmap'] = cmap

    # generate all cells exemplar output map
    ACE_map = all_cells_exemplar_predict(cmap)
    outputs['ACE'] = ACE_map

    # generate foci exemplar output map
    foci_exemplars = make_foci_exemplars(foci_data, language)
    FE_map = foci_exemplar_predict(foci_exemplars)
    outputs['FE'] = FE_map

    # generate foci prototype output map
    foci_prototypes  = make_foci_prototypes(foci_exemplars)
    FP_map = foci_prototype_predict(foci_prototypes)
    outputs['FP'] = FP_map
    
    return outputs

# calculate performance score for output maps over all languages
def calculate_performance_scores(outputs):
    performance_scores = {'ACE' : [], 'FE' : [], 'FP' : []}
    for language in outputs:
        baseline = evaluate(outputs[language]['cmap'], outputs[language]['pmap'])
        ace_performance = evaluate(outputs[language]['ACE'], outputs[language]['pmap'])
        fe_performance = evaluate(outputs[language]['FE'], outputs[language]['pmap'])
        fp_performance = evaluate(outputs[language]['FP'], outputs[language]['pmap'])

        performance_scores['ACE'].append(ace_performance / baseline)
        performance_scores['FE'].append(fe_performance / baseline)
        performance_scores['FP'].append(fp_performance / baseline)

    return performance_scores

# prepare data and plot the scores and lines of best fit
def prepare_and_plot_sorted_scores(performance_scores, foci_data):

    term_sizes_list = []
    for language in range(1, 111):
        term_sizes_list.append(len(universal_terms(foci_data, language)))
    
    # sort all model performance scores
    sorted_ace = sort_in_parallel(performance_scores['ACE'], term_sizes_list)
    sorted_fe = sort_in_parallel(performance_scores['FE'], term_sizes_list)
    sorted_fp = sort_in_parallel(performance_scores['FP'], term_sizes_list)

    # generate scatter plot of values
    spread = range(1, 111)
    scatter_ace = plt.scatter(spread, sorted_ace)
    scatter_fe = plt.scatter(spread, sorted_fe)
    scatter_fp = plt.scatter(spread, sorted_fp)

    # get line of best fit params and correlation metrics for all models
    m_ace, b_ace = line_of_best_fit(spread, sorted_ace)
    best_fit_ace = np.dot(m_ace, spread) + b_ace
    corr_ace, p_ace = sps.pearsonr(best_fit_ace, sorted_ace)

    m_fe, b_fe = line_of_best_fit(spread, sorted_fe)
    best_fit_fe = np.dot(m_fe, spread) + b_fe
    corr_fe, p_fe = sps.pearsonr(best_fit_fe, sorted_fe)

    m_fp, b_fp = line_of_best_fit(spread, sorted_fp)
    best_fit_fp = np.dot(m_fp, spread) + b_fp
    corr_fp, p_fp = sps.pearsonr(best_fit_fp, sorted_fp)
    
    plt.plot(spread, best_fit_ace)
    plt.plot(spread, best_fit_fe)
    plt.plot(spread, best_fit_fp)

    # print out relevant info for all models
    print("All Cells Exemplar model performance [slope, intercept] : {}, correlation coefficient : {}, p-value : {}".format([m_ace, b_ace], corr_ace, p_ace))
    print("Foci Exemplar model performance [slope, intercept] : {}, correlation coefficient : {}, p-value : {}".format([m_fe, b_fe], corr_fe, p_fe))
    print("Foci Prototype model performance [slope, intercept] : {}, correlation coefficient : {}, p-value : {}".format([m_fp, b_fp], corr_fp, p_fp))

    # define legend and plot
    plt.legend((scatter_ace, scatter_fe, scatter_fp),
           ('ACE', 'FE', 'FP'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
    plt.title("Model Performance by Language ")
    plt.xlabel("Languages")
    plt.ylabel("Model Performance")
    plt.show()

# get scores for all 3 models for a specifc language output maps
def get_score(outputs):

    baseline = evaluate(outputs['cmap'], outputs['pmap'])

    ACE = evaluate(outputs['ACE'], outputs['pmap'])
    ACE_performance = ACE / baseline
        
    FE = evaluate(outputs['FE'], outputs['pmap'])
    FE_performance = FE / baseline
        
    FP = evaluate(outputs['FP'], outputs['pmap'])
    FP_performance = FP / baseline
    
    return ACE_performance, FE_performance, FP_performance

# prepare data and graph boxplots
def boxplots(outputs_by_language, foci_data):
    buckets = {}
    # gets all the different number of terms over all languages in dataset
    for language in range(1, 111):
        num_terms = len(universal_terms(foci_data, language))
        if num_terms not in buckets:
            buckets[num_terms] = [outputs_by_language[language]]
        else:
            buckets[num_terms].append(outputs_by_language[language])
    ace_scores = []
    fe_scores = []
    fp_scores = []
    # for each term value, iterate over the maps that contain those many
    # terms and acquire score and store in memory
    for term in buckets:
        ace_term_scores = []
        fe_term_scores = []
        fp_term_scores = []
        for language_outputs in buckets[term]:
            ace, fe, fp = get_score(language_outputs)
            ace_term_scores.append(ace)
            fe_term_scores.append(fe)
            fp_term_scores.append(fp)
        ace_scores.append(np.array(ace_term_scores))
        fe_scores.append(np.array(fe_term_scores))
        fp_scores.append(np.array(fp_term_scores))

    # create boxplots for each model
    box1 = plt.boxplot(ace_scores, patch_artist=True)
    box2 = plt.boxplot(fe_scores, patch_artist=True)
    box3 = plt.boxplot(fp_scores, patch_artist=True)

    # color the boxplots
    colors = ['cyan', 'lightblue', 'lightgreen']
    for patch in box1['boxes']:
        patch.set_facecolor(colors[0])
    for patch in box2['boxes']:
        patch.set_facecolor(colors[1])
    for patch in box3['boxes']:
        patch.set_facecolor(colors[2])

    plt.title("Model Performances by Number of Colour Terms")
    plt.xlabel("Number of Colour Terms")
    plt.ylabel("Model Performance")
    plt.legend([box1['boxes'][0], box2['boxes'][0], box3['boxes'][0]], ['ACE', 'FE', 'FP'], loc='lower left')
    plt.show()

    
    