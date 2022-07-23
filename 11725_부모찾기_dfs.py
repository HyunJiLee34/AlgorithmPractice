import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = {}
ans = {}
visited = [-1 for _ in range(0,N+1)]
for i in range(1,N+1):
    graph[i]=[]

for i in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start]=1
    for i in graph[start]:
        if visited[i]==-1:
            ans[i]=start #트리는 부모가 하나
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(ans[i])