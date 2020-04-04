'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command = input().split()
        if str(command[0]) == "print":
            print(l)
        elif str(command[0]) == "sort":
            l = sorted(l)
        elif str(command[0]) == "pop":
            l.pop()
        elif str(command[0]) == "reverse":
            l.reverse()
        elif str(command[0]) == "insert":
            l.insert(int(command[1]),int(command[2]))
        elif str(command[0]) == "remove":
            l.remove(int(command[1]))
        elif str(command[0]) == "append":
            l.append(int(command[1]))
