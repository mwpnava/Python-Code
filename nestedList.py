

'''
Given the names and grades for each student in a Physics class of  students,
store them in a nested list and print the name(s) of any student(s) having
the second lowest grade.
'''

lista = []
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista+=[[name,score]]
        scorelist+=[score]

min2 = sorted(set(scorelist))[1]
print('\n'.join([a for a,b in sorted(lista) if b == min2]))
