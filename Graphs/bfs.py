from collections import deque
from typing import List

def bfs(adj: List[List[int]], s: int) -> List[int]:
    visited = set()
    ans = []
    q = deque()
    q.append(s)
    visited.add(s)
    while q:
        e = q.popleft()
        ans.append(e)
        for a in adj[e]:
            if a not in visited:
                q.append(a)
                visited.add(a)

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

