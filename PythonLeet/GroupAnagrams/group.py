def group(strs):
    # sorted_words = []
    # for word in strs:
    #     sorted_words.append(''.join(sorted(word)))
    # print sorted_words

    sorted_words = []
    sorted_dict = {}
    for i in range(len(strs)):
        sorted_word  = ''.join(sorted(strs[i]))
        if sorted_word in sorted_dict:
            sorted_dict[sorted_word].append(strs[i])
        else:
            sorted_dict[sorted_word] = [strs[i]]
    for word in sorted_dict:
        sorted_words.append(sorted_dict[word])
    print sorted_words
    return sorted_words
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
group(strs)
