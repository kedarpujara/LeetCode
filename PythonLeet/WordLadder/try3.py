def one_away(w1, w2):
    diff = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff += 1
    return diff == 1

def build_graph(begin_word, end_word, word_list):
    word_list.append(begin_word)

    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            if one_away()