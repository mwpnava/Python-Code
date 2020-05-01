'''
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
'''

from itertools import groupby

#data='1222311'
data='abcabccbadfgzzzz'
data = sorted(data)

for k, g in groupby(data):
    print("{},{}".format(k,len(list(g))))
