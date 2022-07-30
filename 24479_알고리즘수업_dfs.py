import sys
sys.setrecursionlimit(10**6)
n, m, r = map(int, sys.stdin.readline().split())
graph = {}
visited = [0] * (n + 1)
for i in range(1, n + 1):
    graph[i] = []
for j in range(m):
    a, b = map(int,  sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=1
print(graph)
def dfsf(x):
    global cnt
    visited[x]=cnt
    graph[x].sort()
    for i in graph[x]:
        if visited[i] == 0:
            cnt += 1 #방문하니까 cnt+=1
            dfsf(i)


dfsf(r)
for i in range(1, n + 1):
    print(visited[i])