from collections import deque
import sys
a,b = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for i in range(1, a+1):
    graph[i]=[]
for i in range(b):
    N,M = map(int, sys.stdin.readline().rstrip().split())
    graph[N].append(M)
    graph[M].append(N)

visited = [-1 for _ in range(a+1)]


def bfsf(k):
    q = deque([i])
    while q:
        nowNode = q.popleft()
        for now in graph[nowNode]:
            if visited[now]==-1:
                visited[now]=1
                q.append(now)

cnt=0
for i in range(1,a+1):
    print(visited[i])
    if visited[i]==-1:
        bfsf(i)
        cnt+=1
print(cnt)


