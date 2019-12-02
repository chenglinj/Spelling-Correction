import weighted_levenshtein
import numpy as np

dictionary = []
with open('data/dict.txt') as dic:
    for line in dic:
        dictionary.append(line.strip())

misspell = []
with open('data/wiki_misspell.txt') as mis:
    for line in mis:
        misspell.append(line.strip())

correct = []
with open('data/wiki_correct.txt') as cor:
    for line in cor:
        correct.append(line.strip())

delete_costs = np.ones(128, dtype=np.float64)
for i in range(128):
    delete_costs[i] = 3

substitute_costs = np.ones((128, 128), dtype=np.float64)
for i in range(128):
    substitute_costs[i] = np.array([3]*128)

output = []
correct_response = 0
attempted_response = 0
for i in range(0, len(misspell)):
    temp_dis = 6
    temp_word = ''
    count = 0
    for j in range(0, len(dictionary)):
        if abs(len(misspell[i])-len(dictionary[j])) > 5:
            j += 1
        else:
            if weighted_levenshtein.lev(misspell[i], dictionary[j],  delete_costs=delete_costs, substitute_costs=substitute_costs) < temp_dis:
                temp_dis = weighted_levenshtein.lev(misspell[i], dictionary[j], delete_costs=delete_costs, substitute_costs=substitute_costs)
                temp_word = str(dictionary[j])
                count = 1
            elif weighted_levenshtein.lev(misspell[i], dictionary[j], delete_costs=delete_costs, substitute_costs=substitute_costs) == temp_dis:
                temp_word = temp_word + ' ' + str(dictionary[j])
                count += 1

    if correct[i] in temp_word:
        correct_response += 1

    output.append(str(count) + ' ' + temp_word)
    attempted_response += count

    print('For', misspell[i], count, 'correction found')

with open('data/0133_output.txt', 'w') as out:
    for i in range(0, len(output)):
        out.writelines(output[i] + '\n')

print('\nCorrect response: {}'.format(correct_response))
print('Attempted response: {}'.format(attempted_response))
print('Precision:  {:.2%}'.format(correct_response/attempted_response))
print('Recall: {:.2%}'.format(correct_response/len(misspell)))
