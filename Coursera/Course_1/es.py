def matrix_bild(count_word_dict, index_word_dict):
    if index_word_dict == None:
        for key_word in count_word_dict:
            i = count_word_dict.get(key_word)
            return i

    elif count_word_dict == None:
        for frequncy_word in index_word_dict:
            j = index_word_dict.get(frequncy_word)
            return j