from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    
    def addEdge(self, u, v, direction):
        # direction = 0 -> undirected
        # direction = 1 -> directed
        self.adj[u].append(v)

        if direction == 0:  # If the graph is undirected, add the reverse edge
            self.adj[v].append(u)
    
    def printGraph(self):
        for key, values in self.adj.items():
            print(f'{key} -> ', end="")
            for value in values:
                print(f'{value} ', end="")
            print()  # New line for the next vertex

if __name__ == '__main__':
    e = int(input('Enter number of edges: '))
    g = Graph()
    for i in range(e):
        u = int(input(f'Enter starting vertex of edge {i + 1}: '))
        v = int(input(f'Enter ending vertex of edge {i + 1}: '))
        direction = int(input('Enter 0 for undirected or 1 for directed: '))
        g.addEdge(u, v, direction)
    
    # Printing the graph
    print("\nGraph adjacency list:")
    g.printGraph()
