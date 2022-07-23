import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)


maxNum = 0
L = []
def stackf(startNode):
    visited = [-1 for _ in range(N + 1)]
    visited[startNode] = 1
    s = deque([startNode])
    cnt = 0
    while s:
        nowNode = s.pop()
        for i in graph[nowNode]:
            if visited[i] == -1:
                visited[i] = 1
                s.append(i)
                cnt += 1
    return cnt

for i in range(1,N+1):
    cnt = stackf(i)
    if maxNum < cnt :
        L = [i]
        maxNum = cnt
    elif maxNum == cnt :
        L.append(i)
print(*sorted(L))