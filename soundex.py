import jellyfish

dictionary = []
with open('data/dict.txt') as dic:
    for line in dic:
        dictionary.append(line.strip())

dictionary_soundex = []
for i in range(0, len(dictionary)):
    dictionary_soundex.append(jellyfish.soundex(dictionary[i].strip()))

correct = []
with open('data/wiki_correct.txt') as cor:
    for line in cor:
        correct.append(line.strip())

misspell = []
with open('data/wiki_misspell.txt') as mis:
    for line in mis:
        misspell.append(line.strip())

output = []
correct_response = 0
attempted_response = 0
for i in range(0, len(misspell)):
    temp_word = ''
    count = 0
    for j in range(0, len(dictionary_soundex)):

        if jellyfish.soundex(misspell[i]) == dictionary_soundex[j]:
            attempted_response += 1
            temp_word = temp_word + str(dictionary[j]) + ' '
            count += 1
            if dictionary[j] == correct[i]:
                correct_response += 1

    output.append(str(count) + ' ' + temp_word)
    attempted_response += count

    print('For', misspell[i], count, 'correction found')

with open('data/soundex_output.txt', 'w') as out:
    for i in range(0, len(output)):
        out.writelines(output[i] + '\n')

print('\nCorrect response: {}'.format(correct_response))
print('Attempted response: {}'.format(attempted_response))
print('Precision:  {:.2%}'.format(correct_response/attempted_response))
print('Recall: {:.2%}'.format(correct_response/len(misspell)))
