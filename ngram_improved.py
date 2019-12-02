import ngram

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

output = []
correct_response = 0
attempted_response = 0
for i in range(0, len(misspell)):
    temp_dis = 0
    temp_word = ''
    count = 0
    for j in range(0, len(dictionary)):

        if 0.5 <= (len(misspell[i])/len(dictionary[j])) <= 2:

            if ngram.NGram.compare(misspell[i], dictionary[j], N=2) > temp_dis:
                temp_dis = ngram.NGram.compare(misspell[i], dictionary[j], N=2)
                temp_word = str(dictionary[j])
                count = 1
            elif ngram.NGram.compare(misspell[i], dictionary[j], N=2) == temp_dis:
                temp_word = temp_word + ' ' + str(dictionary[j])
                count += 1

        else:
            j += 1

    if correct[i] in temp_word:
        correct_response += 1

    output.append(str(count) + ' ' + temp_word)
    attempted_response += count

    print('For', misspell[i], count, 'correction found')

with open('data/ngram_output.txt', 'w') as out:
    for i in range(0, len(output)):
        out.writelines(output[i] + '\n')

print('\nCorrect response: {}'.format(correct_response))
print('Attempted response: {}'.format(attempted_response))
print('Precision:  {:.2%}'.format(correct_response/attempted_response))
print('Recall: {:.2%}'.format(correct_response/len(misspell)))