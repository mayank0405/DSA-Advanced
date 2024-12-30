def dfs_rec(source, visited, adj, ans):
    visited[source] = True
    ans.append(source)
    for child in adj[source]:
        if not visited[child]:
            dfs_rec(child, visited, adj, ans)


def dfs(adj):
    visited = [False]*len(adj)
    ans = []
    for i in range(len(adj)):
        if not visited[i]:
            dfs_rec(i, visited, adj, ans)

    return ans