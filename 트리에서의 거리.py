n,x,y = map(int,input().split())
graph ={}
cnt=0
ans=0
visited=[-1 for _ in range(n)]
for i in range(0,n+1):
    graph[i]=[]
for _ in range(n-1):
    n,m = map(int,input().split())
    graph[n].append(m)
    graph[m].append(n)
def dfs(a):
    global cnt
    global ans
    visited[a]=1
    if a == y:
        ans = cnt
    for i in graph[a]:
        if visited[i]==-1:
            cnt+=1
            dfs(i)
            cnt-=1

    # b에 갈때까지 cnt한다


dfs(x)
print(ans)