from collections import deque
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)
maxNum = -1
L=[]
def dfs(nowNode):
    global cnt
    for toNode in graph[nowNode]:
        if visited[toNode]==-1:
            visited[toNode]=1
            cnt+=1
            dfs(toNode)

for i in range(1,N+1):
    visited=[-1 for _ in range(N+1)]
    cnt=0
    dfs(i)

    if maxNum < cnt :
        L = [i]
        maxNum = cnt
    elif maxNum == cnt :
        L.append(i)
print(L)