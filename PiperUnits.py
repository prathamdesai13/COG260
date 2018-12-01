# probability map
# generates a superimposed map of all the colour maps elicited from speakers of a language,
# for evaluation of prediction models

LANGUAGE = 1

def prob_map(data, language):
    """
    Constructs language map for each participant which
    """
    count_map = {}
    for speaker in data[language]:
        for cell in data[language][speaker]:
            colour = data[language][speaker][cell]
            if cell not in count_map:
                count_map[cell] = {colour: 1}
            else:
                if colour not in count_map[cell]:
                    count_map[cell][colour] = 1
                else:
                    count_map[cell][colour] += 1
    return count_map

# returns score of how well the prediction_map matches the prob_map
def score(prob_map, prediction_map):
    pass
 
