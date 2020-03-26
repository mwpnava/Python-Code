'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
'''

def compressString(strg):

    lenght = len(strg)

    #Edge case 1
    if lenght == 0:
        return ""

    #Edge case 2
    if lenght == 1:
        return strg + "1"

    compressStr = ""
    counter = 1
    i = 1

    while i < lenght:

       if strg[i-1] == strg[i]:
           counter += 1
       else:
           compressStr = compressStr + strg[i-1] + str(counter)
           counter = 1

       i+=1

    compressStr = compressStr + strg[i-1] + str(counter)

    return compressStr


x = compressString('AAABCa')
print(x)
