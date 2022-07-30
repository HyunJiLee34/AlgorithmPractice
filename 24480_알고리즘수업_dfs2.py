import sys
sys.setrecursionlimit(10**6)
n,m,r = map(int, sys.stdin.readline().split()) #정점 수, 간선 수, 시작정점
graph = {}
visited = [0]*(n+1)
cnt=1
for i in range(1, n+1):
    graph[i]=[]

for j in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfsf(x):
    global cnt
    visited[x]=cnt
    graph[x].sort(reverse=True)
    for i in graph[x]:
        if visited[i]==0:
            cnt+=1
            dfsf(i)



dfsf(r)
for i in range(1, n + 1):
    print(visited[i])

