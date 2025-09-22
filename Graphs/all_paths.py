def dfs(adj, visited, target, path, node):
    if node == target:
        print(path)
        return 
    for neighbor in adj[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(adj, visited, target, path + str(neighbor), neighbor)
            visited.remove(neighbor)

path = ''
visited = set()
adj = [[1,2],[3],[3],[]]
target = 3
dfs(adj, visited, target, path, 0)


