def plusMinus(arr):
    '''
    Given an array of integers, it calculates the fractions of its elements that are positive,
    negative, and are zeros.
    Param: Array of integers
    Return: Print the decimal value of each fraction on a new line
    '''

    n = len(arr)

    if n==0:
        raise Exception("Array is empty")

    positive,negative,neutral = 0,0,0

    for element in arr:
        if element == 0:
            neutral +=1
        elif element > 0:
            positive+=1
        elif element < 0:
            negative+=1

    print(round(positive/n,6))
    print(round(negative/n,6))
    print(round(neutral/n,6))


#testing
plusMinus([2,2,1,-1,-1,0])
