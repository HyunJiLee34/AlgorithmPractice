n,r=map(int,input().split())
graph = {}
cnt=0
maxcnt=0
visited = [-1 for _ in range(n+1)]
for i in range(0,n):
    graph[i]=[]
for _ in range(n-1):
    N,M = map(int, input().split())
    graph[N].append(M)
    graph[M].append(N)

def dfs(x):
    global maxcnt
    global cnt
    visited[x]=1
    for i in graph[x]:
        if visited[i]==-1:
            visited[i]=1
            cnt+=1
            dfs(i)
            if cnt > maxcnt:
                maxcnt = cnt
            cnt-=1


dfs(r)
print(maxcnt)
