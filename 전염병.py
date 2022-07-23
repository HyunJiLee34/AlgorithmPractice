from collections import deque
n,k = map(int,input().split())

visited = [-1 for _ in range(n+1)]
def bfs(x):
    global visited
    q= deque()
    q.append(x)
    visited[x]=x
    while q:
        nownode = q.popleft()
        next1 = nownode*2
        next2 = nownode//3
        if 0<next1<=n and visited[next1]==-1:
            visited[next1]=next1
            q.append(next1)
        if 0<next2<=n and visited[next2]==-1:
            visited[next2]=next2
            q.append(next2)

bfs(k)
cnt=0
for i in range(1,len(visited)):
    if visited[i]==-1:
        cnt+=1
print(cnt)