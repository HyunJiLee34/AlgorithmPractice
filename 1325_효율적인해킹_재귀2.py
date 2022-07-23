from collections import deque
N,M = map(int, sys.stdin.readline().rstrip().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    a,b = map(int, input().split())
    graph[b].append(a)

cnt=0
maxnum = 0
def bfsf(nowNode):
    global cnt
    for now in graph[nowNode]:
        if visited[now]==-1:
            visited[now]=1
            cnt+=1
            bfsf(now)

ans = []
for i in range(1,N+1):
    visited = [-1 for _ in range(N + 1)]
    cnt=0
    bfsf(i)
    if maxnum < cnt:
        ans = [i]
        maxnum = cnt
    elif maxnum == cnt:
        ans.append(i)

print(*ans)

