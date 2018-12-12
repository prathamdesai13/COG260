from PrathUnits import *
from PiperUnits import *
from wcs_helper_functions import *
from time import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

# get data
foci_data = readFociData('./WCS_data_core/foci-exp.txt')
namingData = readNamingData('./WCS_data_core/term.txt')

# model performances saved in array format
ACE_performances = [0.9272807404142792, 0.9425780319275681, 0.9159245678365638, 0.9587149499788646, 0.9077238550922765, 0.9296590177997004, 0.938583815028902, 0.9379460745440125, 0.9423047877964055, 0.9560099132589842, 0.9422073079791204, 0.9446414803392447, 0.9549655850540807, 0.9742143432715553, 0.9556524900036352, 0.9525169582292038, 0.935141316778304, 0.9101986754966885, 0.9292946927374309, 0.9343702579666167, 0.9614163226421089, 0.9474647629507601, 0.9567964480874317, 0.9161526921153526, 0.953099059214167, 0.9589689637033137, 0.9217745392198886, 0.9343856979840244, 0.9430155552133065, 0.957933090427294, 0.9873631002527379, 0.9385981135565009, 0.8331914893617017, 0.9592451314996983, 0.9350174216027873, 0.981726879620589, 0.9506344515904744, 0.9082969432314408, 0.9357696566998889, 0.9475734458691779, 0.9613445378151262, 0.9463703099510602, 0.9351363740545491, 0.9434167573449406, 0.9478422850046568, 0.9418188022521754, 0.9559671500961041, 0.9221982758620689, 0.9306585259485385, 0.9477298740938577, 0.9479166666666673, 0.9521390896659506, 0.7442145862552588, 0.9451697127937335, 0.9347654710287738, 0.9692118226600985, 0.9436063218390803, 0.9478776529338334, 0.906103286384977, 0.9580061454421304, 0.9045936395759715, 0.9302712993812476, 0.9402241594022408, 0.9544550517104214, 0.9571933742788011, 0.9402390438247019, 0.9180366928758631, 0.9498658964307818, 0.9431970830934558, 0.934604904632153, 0.9588108287659858, 0.9627048408363155, 0.933230769230769, 0.9286556603773582, 0.9445398351648355, 0.9341192787794729, 0.9632798573975041, 0.9070707070707067, 0.9487532507266335, 0.9544379631089386, 0.9703153988868272, 0.9708299096138048, 0.9267075978511128, 0.951417848206839, 0.9616483681756656, 0.8216905344044709, 0.957829046898638, 0.9550281074328547, 0.9679445876288657, 0.9663345929233939, 0.9105851413543722, 0.9384277075316108, 0.9207108680792887, 0.9446102819237148, 0.9410906438081346, 0.9505932065659025, 0.9105385060799069, 0.9533434076312809, 0.9640959587828046, 0.9670838333619063, 0.968878121505777, 0.9365384615384617, 0.9353435778486512, 0.9766361524798471, 0.9587429046102733, 0.9333104159504987, 0.9673569673569674, 0.9458373513339761, 0.9630984042553191, 0.9464648041204932]
FE_performances = [0.5702952842661966, 0.6533238027162267, 0.47118910424305915, 0.5095110610116953, 0.6206425153793572, 0.46386446493673716, 0.672326589595376, 0.57355273592387, 0.6366107838695048, 0.4950433705080547, 0.7211036539895609, 0.7107170393215113, 0.4902654867256638, 0.4264302981466562, 0.663940385314431, 0.7620492681185294, 0.7098513314817844, 0.39602649006622404, 0.6895949720670395, 0.6631259484066786, 0.5949507780247697, 0.8140215998535608, 0.7846653005464483, 0.7219536589431563, 0.7668788046485886, 0.7027880063124672, 0.5482211744534939, 0.6285659946747821, 0.6941321423071001, 0.7856906260351114, 0.12987924740241483, 0.8035879415572412, 0.7018439716312054, 0.6265810078297523, 0.5806620209059233, 0.8320546798716695, 0.6673040152963673, 0.7580058224163033, 0.526467331118494, 0.6870637883460494, 0.6797555385790681, 0.490619902120718, 0.5358698143479257, 0.640914036996736, 0.7654455138155853, 0.7198430301996248, 0.7272409575397524, 0.5137931034482752, 0.7193632795464457, 0.7272033574971386, 0.710536858974359, 0.5233444032037506, 0.6539270687237023, 0.5685880698935531, 0.4954670871107612, 0.570900774102745, 0.7077945402298854, 0.6367041198501869, 0.461032863849766, 0.4580061454421311, 0.5838241067923051, 0.4543074726320804, 0.4752179327521788, 0.5902943516308675, 0.5693281220919407, 0.3436623874870889, 0.5184655706456992, 0.7817206519496593, 0.5699481865284973, 0.5155313351498642, 0.6382660687593421, 0.6001130156338298, 0.5883076923076928, 0.7875884433962265, 0.7117101648351647, 0.3259361997226074, 0.49316696375519925, 0.525925925925925, 0.6721737800214168, 0.6950969572757362, 0.7523191094619668, 0.5435497124075601, 0.4915579432079814, 0.5218932443703085, 0.6306211460369977, 0.5764931889626267, 0.6374810892586997, 0.7191338746616694, 0.5314110824742262, 0.7408107179663348, 0.5450361604207757, 0.655305112699286, 0.35748462064251535, 0.6582089552238805, 0.5737734816706181, 0.5507882333820904, 0.5208453966415743, 0.7109935776350592, 0.6127837707293513, 0.7061546374078521, 0.696608274319791, 0.36403846153846214, 0.5746593215424756, 0.39185681103975967, 0.544510591167107, 0.7767273977311795, 0.7209547209547212, 0.7020250723240119, 0.8118351063829788, 0.7026689558295615]
FP_performances = [0.705817540766858, 0.461758398856326, 0.7448926139339979, 0.5575595321967027, 0.6794258373205742, 0.3289727643148195, 0.604768786127168, 0.7733941316415543, 0.6319287116749728, 0.4452705493597689, 0.7287472035794191, 0.7796453353893603, 0.44660766961651915, 0.2894439967767929, 0.6308615049073061, 0.7493752231345949, 0.6214670805423949, 0.5650331125827811, 0.5998603351955311, 0.7037177541729915, 0.5462051444903149, 0.8050521691378365, 0.774760928961749, 0.6247707951325214, 0.6216104039845046, 0.6656145888129058, 0.476639519931419, 0.5127424876378855, 0.8429077468042508, 0.8456442530639289, 0.11878685762426273, 0.31126317736267795, 0.6663829787234035, 0.5916482634009235, 0.6437282229965154, 0.7662156507183706, 0.7333565096471402, 0.604075691411936, 0.5545957918050938, 0.7258561921765965, 0.579067990832697, 0.5772838499184343, 0.3185881274352502, 0.5699129488574541, 0.6735485873952191, 0.6236137177955984, 0.7190284815656132, 0.4885775862068964, 0.7248146532926293, 0.6676840900419687, 0.3050881410256405, 0.34811486618480164, 0.5305049088359044, 0.42920265113476586, 0.670082774931021, 0.5198803659394797, 0.693247126436782, 0.617353308364544, 0.43403755868544647, 0.4598839194264259, 0.2877895563407933, 0.48833888624464605, 0.12777085927770832, 0.29017501988862354, 0.7249209008002974, 0.40239043824701193, 0.4662854419823683, 0.7728491850629254, 0.5308002302820956, 0.401816530426885, 0.5475834578973591, 0.585232623846299, 0.4726153846153853, 0.8494988207547175, 0.6698145604395608, 0.17730004623208512, 0.6906714200831849, 0.6094276094276087, 0.7046045586660551, 0.6055494245625096, 0.6231910946196665, 0.4531635168447004, 0.4589409056024562, 0.5241868223519598, 0.5802376297187544, 0.5736989172196999, 0.5711043872919818, 0.536956069123465, 0.7076353092783504, 0.7636551013397457, 0.6252465483234714, 0.6184716877405175, 0.36431989063567993, 0.7243781094527362, 0.4517599854094473, 0.487079473427597, 0.42848870874348555, 0.7058934642992072, 0.6234100788922877, 0.8138179324532833, 0.7346254193067457, 0.34134615384615413, 0.27486227892142595, 0.5742587785216561, 0.7991139415755241, 0.8114472327260227, 0.7371007371007369, 0.7402764384442302, 0.3633643617021278, 0.6886218198845014]

def line_of_best_fit(x, y):

    return np.polyfit(x, y, deg=1)

def sort_in_parallel(to_sort, indices):

    return [x for _, x in sorted(zip(indices, to_sort))]

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
    return ACE_performances, FE_performances, FP_performances

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

def prepare_and_plot_sorted_scores(performance_scores, foci_data):

    term_sizes_list = []
    for language in range(1, 111):
        term_sizes_list.append(len(universal_terms(foci_data, language)))

    sorted_ace = sort_in_parallel(performance_scores['ACE'], term_sizes_list)
    sorted_fe = sort_in_parallel(performance_scores['FE'], term_sizes_list)
    sorted_fp = sort_in_parallel(performance_scores['FP'], term_sizes_list)

    spread = range(1, 111)
    scatter_ace = plt.scatter(spread, sorted_ace)
    scatter_fe = plt.scatter(spread, sorted_fe)
    scatter_fp = plt.scatter(spread, sorted_fp)

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
    

if __name__ == "__main__":
    # outputs_by_language = {}
    # for language in range(1, 111):
    #     print("Language - {}".format(language))
    #     outputs = pipeline(namingData, foci_data, 1)
    #     outputs_by_language[language] = outputs
    # performance_scores = calculate_performance_scores(outputs_by_language)
    ACE_performances, FE_performances, FP_performances = get_model_scores(namingData, foci_data)
    # print(ACE_performances)
    # print("-------------------------------------------")
    # print(FE_performances)
    # print("-------------------------------------------")
    # print(FP_performances)
    # print("-------------------------------------------")
    prepare_and_plot_sorted_scores({'ACE' : ACE_performances, 'FE' : FE_performances, 'FP' : FP_performances}, foci_data)
    