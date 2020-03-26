def staircase(n):

    '''
    It prints a staircase that its base and height are both equal to n,
    and the image is drawn using # symbols and spaces.
    The last line is not preceded by any spaces.

    param: integer
    return: print n number of lines to create the 'staircase'
    '''
    #Edge case
    if not isinstance(n, int) or n == 0:
        raise Exception('Incorrect input')

    c1,c2 = n - 1,1

    for num in range(n):
        print('{}{}'.format(' ' * c1,'#' * c2))
        c1-=1
        c2+=1


#Testing function
staircase(100)
