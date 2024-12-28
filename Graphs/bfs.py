from collections import deque
from typing import List

def bfs(adj: List[List[int]], s: int) -> List[int]:
    n = len(adj)
    visited = [False] * n
    ans = []
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        e = q.popleft()
        ans.append(e)
        for a in adj[e]:
            if not visited[a]:
                q.append(a)
                visited[a] = True

    return ans


adj1 = [
    [1, 2],
    [0, 3, 4],
    [0, 5],
    [1],
    [1],
    [2]
]

bfs_traversal = bfs(adj1, 0)

print(bfs_traversal)


#Answer -> [0, 1, 2, 3, 4, 5]

