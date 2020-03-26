'''
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.
Approach 2
'''


def missingValue(arr1, arr2):

    return sum(arr1) - sum(arr2)


x = missingValue([1,2,5,3,4],[1,2,3,5])
print(x)
