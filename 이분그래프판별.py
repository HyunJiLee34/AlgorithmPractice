N,M = map(int,input().split())
graph = {}
flag=True
visited = [0 for _ in range(N+1)]

for i in range(0,N+1):
    graph[i]=[]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,side):
    global visited, graph, flag
    visited[x]=side
    for i in graph[x]:
        if visited[i]!=0 and visited[i]==side:
            flag=False
            return
        if side == 1:
            side2 = -1
        else :
            side2 = 1
        if visited[i]==0:
            dfs(i,side2)

dfs(1,1)
if flag :
    print('YES')
else :
    print("NO")