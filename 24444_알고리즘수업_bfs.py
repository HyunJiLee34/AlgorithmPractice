import sys
from collections import deque
sys.setrecursionlimit(10**6)
n,m,r = map(int, sys.stdin.readline().split()) #정점 수, 간선 수, 시작정점
graph = {}
visited = [0]*(n+1)
visited[r]=1
queue = deque([r])
cnt=1
for i in range(1, n+1):
    graph[i]=[]

for j in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,n+1):
    graph[i].sort()

while queue :
    v= queue.popleft()
    for i in graph[v]:
        if visited[i]==0:
            queue.append(i)
            cnt += 1
            visited[i] = cnt
            
for i in range(1, n + 1):
    print(visited[i])