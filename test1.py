N = int(input())
M = int(input())
graph = {}
cnt=0
visited = [-1 for _ in range(N+1)]
for i in range(1,N+1):
    graph[i]=[]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1]=0
def dfs(x):
    global cnt
    for i in graph[x]:
        if visited[i]==-1:
            visited[i]=1
            cnt+=1
            dfs(i)


dfs(1)
print(cnt)
