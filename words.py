'''
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
'''



def howmanywords(n):

    dictionary = {}
    for x in range(n):
        word = input()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    print(len(dictionary))

    #Print in just one line, all dictionary values
    print(*dictionary.values())


howmanywords(int(input()))
