from collections import defaultdict

#Unweighted Undirected Graph
def unweighted_undirected():
    e = int(input('Enter number of edges '))
    adj_list = defaultdict(list)
    for i in range(e):
        u,v = list(map(int, input('Enter the source and destination of the edge ').split(' ')))
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    print(adj_list)

unweighted_undirected()

#Unweighted directed graph
def unweighted_directed():
    e = int(input('Enter number of edges: '))
    adj_list = defaultdict(list)
    for i in range(e):
        u,v = list(map(int, input('Enter the source and destination of the edge: ').split(' ')))
        adj_list[u].append(v)

    print(adj_list)

unweighted_directed()

#Weighted undirected graph
def weighted_undirected():
    e = int(input('Enter number of edges: '))
    adj_list = defaultdict(list)
    for i in range(e):
        u,v,w = list(map(int, input('Enter the source, destination and weight of the edge: ').split(' ')))
        adj_list[u].append([v,w])
        adj_list[v].append([u,w])
    
    print(adj_list)

weighted_undirected()

#Weighted directed graph
def weighted_directed():
    e = int(input('Enter number of edges: '))
    adj_list = defaultdict(list)
    for i in range(e):
        u,v,w = list(map(int, input('Enter the source, destination and the weight of the edge: ').split(' ')))
        adj_list[u].append([v,w])
    
    print(adj_list)

weighted_directed()


