#Unweighted Undirected Graph
def unweighted_undirected():
    vertex, edges = list(map(int, input('Enter number of vertices then number of edges: ').split()))
    adjList = [[] for _ in range(vertex)]
    for i in range(edges):
        u,v = list(map(int, input('Enter u then v: ').split()))
        adjList[u].append(v)
        adjList[v].append(u)
    
    for i in range(vertex):
        print(f'{i} -> ', end = '')
        for j in range(len(adjList[i])):
            print(adjList[i][j], end = ' ')
        print()

#Unweighted Directed Graph
def unweighted_directed():
    vertex, edges = list(map(int, input('Enter number of vertices then number of edges: ').split()))
    adjList = [[] for _ in range(vertex)]
    for i in range(edges):
        u,v = list(map(int, input('Enter u then v: ').split()))
        adjList[u].append(v)
    
    for i in range(vertex):
        print(f'{i} -> ', end = '')
        for j in range(len(adjList[i])):
            print(adjList[i][j], end = ' ')
        print()

#Weighted Undirected Graph
def weighted_undirected():
    vertex, edges = list(map(int, input('Enter number of vertices then number of edges: ').split()))
    adjList = [[] for _ in range(vertex)]
    for i in range(edges):
        u,v,w = list(map(int, input('Enter u then v then weight: ').split()))
        adjList[u].append((v, w))
        adjList[v].append((u, w))
    
    for i in range(vertex):
        print(f'{i} -> ', end = '')
        for j in range(len(adjList[i])):
            print(adjList[i][j], end = ' ! ')
        print()

#Weighted Directed Graph
def weighted_directed():
    vertex, edges = list(map(int, input('Enter number of vertices then number of edges: ').split()))
    adjList = [[] for _ in range(vertex)]
    for i in range(edges):
        u,v,w = list(map(int, input('Enter u then v then weight: ').split()))
        adjList[u].append((v, w))
    
    for i in range(vertex):
        print(f'{i} -> ', end = '')
        for j in range(len(adjList[i])):
            print(adjList[i][j], end = ' ! ')
        print()


if __name__ == '__main__':
    print(('Enter the number of type of graph: \n 1-> Unweighted Undirected Graph \n 2-> Unweighted Directed Graph \n 3-> Weighted Undirected Graph \n 4-> Weighted Directed Graph'))
    n = int(input())
    if n == 1:
        unweighted_undirected()
    elif n == 2:
        unweighted_directed()
    elif n == 3:
        weighted_undirected()
    elif n == 4:
        weighted_directed()
    else:
        print('Wrong output!!!')