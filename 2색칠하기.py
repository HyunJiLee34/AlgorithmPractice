N,M = map(int,input().split())
graph = {}
flag=True
visited = [0 for _ in range(N)]
print(visited)#색칠 안되어있으면 -1 되어있으면 0 혹은 1
for i in range(0,N+1):
    graph[i]=[]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x,color):
    global graph, visited, flag
    visited[x]=color

    for i in graph[x]:

        if visited[i]!=0 and visited[i]==color:
            flag=False
            return
        if color==1 :
            color2=-1
        else :
            color2=1
        if visited[i]==0:
            dfs(i, color2)

dfs(0,1)

if flag:
    print('YES')
else:
    print('NO')

