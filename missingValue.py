'''
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.
Approach 1
'''


def missingValue(arr1, arr2):

    #Edge case
    if len(arr1) == len(arr2):
        print('Arrays with same lenght')


    for element in arr1:

        if element not in arr2:
            return element

    return 0


x = missingValue([1,2,3,4],[1,2,3])
print(x)
