'''
Implementin a BFS (​breadth-first search) in Python
'''

tree = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : ['L'],
  'G' : ['I','H'],
  'I' : [],
  'L' : [],
  'H' : [] 
}


def BSF(tree,root):

    visited = []
    fifo = []

    visited.append(root)
    fifo.append(root)

    while fifo:

        first = fifo.pop(0)
        print(first,end=' ')

        for child in tree[first]:
            if child not in visited:
                fifo.append(child)
                visited.append(child)



BSF(tree,'A')
