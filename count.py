def my_func(words):
    ctr = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            list.append(word)
    print("List of word with the same first and last character",list)
    return ctr
count = my_func(["abc","cfc","hjk","bab","cac"])
print("Number of words with same first and last character:",count)
