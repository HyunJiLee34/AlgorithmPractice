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


def dfsf(k):
    visited[k]=1
    for i in graph[k]:
        if visited[i]==-1:
            visited[i]=1
            dfsf(i)

cnt=0
for i in range(1,b+1):
    if visited[i]==-1:
        dfsf(i)
        cnt+=1
print(cnt)



