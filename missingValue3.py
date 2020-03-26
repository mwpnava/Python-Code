'''
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.
Approach 3
'''


def missingValue(arr1,arr2):

    arr1.sort()
    arr2.sort()

    for n1,n2 in zip(arr1,arr2):

        if n1 != n2:
            return n1

    return arr1[-1]


x = missingValue([1,4,3,2,5],[1,5,2,3])
print(x)
