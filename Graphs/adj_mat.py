#Unweighted Undirected Graph
def adj_unweighted_undirected():
    vertex = int(input('Enter number of vertices: '))
    edges = int(input('Enter number of edges: '))
    adj = [[0]*vertex for _ in range(vertex)]
    for i in range(edges):
        u,v = list(map(int, input('Enter u then v: ').split()))
        adj[u][v] = 1
        adj[v][u] = 1
    
    for i in range(vertex):
        for j in range(vertex):
            print(adj[i][j], end = ' ')
        print()

#Weighted Undirected Graph
def adj_weighted_undirected():
    vertex = int(input('Enter number of vertices: '))
    edges = int(input('Enter number of edges: '))
    adj = [[0]*vertex for _ in range(vertex)]
    for i in range(edges):
        u,v,w = list(map(int, input('Enter u then v then weight: ').split()))
        adj[u][v] = w
        adj[v][u] = w
    
    for i in range(vertex):
        for j in range(vertex):
            print(adj[i][j], end = ' ')
        print()

#Unweighted Directed Graph
def adj_unweighted_directed():
    vertex = int(input('Enter number of vertices: '))
    edges = int(input('Enter number of edges: '))
    adj = [[0]*vertex for _ in range(vertex)]
    for i in range(edges):
        u,v = list(map(int, input('Enter u then v: ').split()))
        adj[u][v] = 1
    
    for i in range(vertex):
        for j in range(vertex):
            print(adj[i][j], end = ' ')
        print()

#Weighted Directed Graph
def adj_weighted_directed():
    vertex = int(input('Enter number of vertices: '))
    edges = int(input('Enter number of edges: '))
    adj = [[0]*vertex for _ in range(vertex)]
    for i in range(edges):
        u,v,w = list(map(int, input('Enter u then v then w: ').split()))
        adj[u][v] = w
    
    for i in range(vertex):
        for j in range(vertex):
            print(adj[i][j], end = ' ')
        print()


if __name__ == '__main__':
    print(('Enter the number of type of graph: \n 1-> Unweighted Undirected Graph \n 2-> Unweighted Directed Graph \n 3-> Weighted Undirected Graph \n 4-> Weighted Directed Graph'))
    n = int(input())
    if n == 1:
        adj_unweighted_undirected()
    elif n == 2:
        adj_unweighted_directed()
    elif n == 3:
        adj_weighted_undirected()
    elif n == 4:
        adj_weighted_directed()
    else:
        print('WRONG INPUT!!!!!!')
