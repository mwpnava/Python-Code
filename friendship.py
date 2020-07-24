from datetime import datetime

'''
Given 2 arrays, starts and ends, with friends numbers id and the start date and end date of
their friendship.

starts = [[1,2,'2001-05-1'],[1,2,'2006-05-1'],[1,3,'2001-05-1'],[3,4,'2006-05-1'],[1,3,'2020-05-1']]
ends = [[1,2,'2005-04-10'],[2,1,'2009-05-1'],[3,1,'2007-12-1']]

Create a function to return friends and dates of start and end friendship

Outcome:

(1,2,'2001-05-1','2005-04-10')
(1,2,'2006-05-1','2009-05-1')
(1,3,'2001-05-1','2007-12-1')

friends 3 & 4, and 1 & 3 are still friends at this time
'''



def createDictionary(arr):

    '''
    Create a dictionary with data from an array
    '''

    dict_temp = {}
    for element in arr:
        element = list(element)
        friend1, friend2, dateStatus = element[:]
        dateStatus =  datetime.strptime(dateStatus, '%Y-%m-%d')
        key_friend =  str(min(friend1,friend2)) + '-' + str(max(friend1,friend2))

        if key_friend in dict_temp:
            dict_temp[key_friend].append(dateStatus)
        else:
            dict_temp[key_friend] = [dateStatus]

    return dict_temp



def friendsRelation(starts,end):

    '''
    Args: two arrays
        starts = [[id_user, id_anotheruser,start date friendship]]
        ends = [[id_user, id_anotheruser,end date friendship]]

    Returns: Print pairs of friends and start and end dates of friendship

    '''

    all_dates = starts + ends
    completeDict = createDictionary(all_dates)

    for relation,values in completeDict.items():

        action_dates = sorted(values, reverse=False)
        f1,f2 = relation.split('-')
        limit = len(action_dates)
        if len(action_dates) % 2 != 0:
            limit = len(action_dates) - 1

        i=0
        while i < limit:

            print("({}, {}, {}, {})".format(f1,f2,
                action_dates[i].strftime('%Y-%m-%d'),
                action_dates[i+1].strftime('%Y-%m-%d')))
            i+=2



starts = [[1,2,'2001-05-1'],[1,2,'2006-03-10'],[1,3,'2001-02-14'],[3,4,'2006-05-1'],[1,3,'2020-10-05']]
ends = [[1,2,'2005-04-10'],[2,1,'2009-11-01'],[3,1,'2007-12-1']]


friendsRelation(starts,ends)
