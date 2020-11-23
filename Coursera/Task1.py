import collections
import re
import numpy as np
from scipy.spatial import distance


general_string = ''
sentence_list = []
dict_unique = {}
index_word = 0

with open('sentences.txt') as f_read:
    for line in f_read:
        line = line.lower()
        sentence_list.append(re.split(r'[^a-z]', line))

    w_dict = collections.Counter()
    for line_list in sentence_list:
        while '' in line_list:
            line_list.remove('')

        if len(line_list) == 0:
            sentence_list.remove(line_list)

        for word in line_list:
            if word not in dict_unique:
                dict_unique[word] = index_word
                index_word += 1

        for word in line_list:
            w_dict[word] += 1

matrix = np.zeros((len(sentence_list), len(dict_unique)))  # , dtype=np.float32)

# result_list = []
for line in sentence_list:
    for word in line:
        index_for_matrix = dict_unique.get(word)
        matrix[sentence_list.index(line)][index_for_matrix] += 1

result = ''
with open('result.txt', 'w') as file:
    for sentence in matrix[1:]:
        result = distance.cosine(matrix[0], matrix[sentence]) + ''
        file.write(result)




# print(dict_unique, '\n')
#
# for line in sentence_list:
#     print(line)
#
# print('\n')
# print(matrix)
