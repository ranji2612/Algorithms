def BFS(a,startNode):
    #a is the adjacency List
    #-----------------BFS-------------------
    q = []
    d = [-1 for x in range(len(a))]
    #Starting with the first node
    q.append(startNode)
    d[startNode] = 0
    
    while (len(q) > 0):
        node = q.pop(0)
        for x in a[node]:
            if d[x]==-1:
                d[x] = d[node]+1
                q.append(x)
        print 'processing node ',node
    print d

def DFS(a,startNode):
    #a is the adjacency List
    #----------------DFS-----------------
    q = []
    d = [-1 for x in range(len(a))]
    #Starting with the first node
    q.append(startNode)
    d[startNode] = 0
    
    while (len(q) > 0):
        node = q.pop(0)
        for x in a[node]:
            if d[x]==-1:
                d[x] = d[node]+1
                q.insert(0,x)
        print 'processing node ',node

#Graph Adjacency List
a =[ [2],[2],[0,1,3],[2,4,5],[3,6],[3],[4,7],[6] ]
#Undirected Graph - Printing the edges
for i in range(len(a)):
    for k in a[i]:
        if i < k:
            print i,' -> ',k
BFS(a,7)
