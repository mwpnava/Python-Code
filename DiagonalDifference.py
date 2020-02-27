def diagonalDifference(arr):

    '''
    Given a square matrix, this function calculates the absolute difference
    between the sums of its diagonals.
    Param: 2D Array (The matrix)
    Return: An integer (The result of sums of matrix's diagonals)
    '''

    #Edge case
    if len(arr) == 0:
        return 0

    sum1,sum2,i2 = 0,0,len(arr) -1

    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][i2]
        i2 -= 1

    return abs(sum1 - sum2)


#Testing function
X = [[11,2,4],[4,5,6],[10,8,-12]]
result = diagonalDifference(X)
print(result)
