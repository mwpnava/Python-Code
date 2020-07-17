
def numIdenticalPairs(nums):

    '''
    Given an array of integers nums, return the number of good pairs.
    A pair (i,j) is called good if nums[i] == nums[j] and i < j.

    Args: an array of integers nums.
    Returns: an integer
    '''


    dict = {}
    result = 0
    ind = 0

    for num in nums:

        if num in dict:
            dict[num].append(ind)
        else:
            dict[num] = [ind]
        ind += 1

    for k in dict.keys():
        x = 0
        if len(dict[k]) > 0 :
            i = len(dict[k])
            while i > 0:
                i-=1
                x += i

        result += x

    return result

r = numIdenticalPairs([1,2,3,1,1,2,3])
print(r)
