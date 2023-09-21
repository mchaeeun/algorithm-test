import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [ [] for i in range(n)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1] += set([y]) - set(graph[x - 1])
    graph[y - 1] += set([x]) - set(graph[y - 1])
    
# DFS
stack = deque([v])
visited_dfs = deque()
while stack:
    cur = stack.pop()
    if cur not in visited_dfs:
        tmp = list(set(graph[cur - 1]) - set(visited_dfs))
        tmp.sort(reverse=True)
        stack += tmp
        visited_dfs.append(cur)

while visited_dfs:
    print(visited_dfs.popleft(), end=" ")

print("\n", end="")
# BFS
queue = deque([v])
visited_bfs = deque()
while queue:
    cur = queue.popleft()
    if cur not in visited_bfs:
        tmp = list(set(graph[cur - 1]) - set(visited_bfs))
        tmp.sort()
        queue += tmp
        visited_bfs.append(cur)

while visited_bfs:
    print(visited_bfs.popleft(), end=" ")