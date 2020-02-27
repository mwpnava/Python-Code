def diagonalDifference(arr):
    sum1,sum2 = 0,0
    i2 = len(arr) -1

    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][i2]
        i2 -= 1

    return abs(sum1 - sum2)


#Testing function

X = [[11,2,4],[4,5,6],[10,8,-12]]
result = diagonalDifference(X)
print(result)
