from collections import deque
import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
q = deque([])
ansL = []
visited = [-1 for _ in range(N+1)]
for i in range(1,N+1):
    q.append([i])
while q :
    nowL = q.popleft()
    if len(nowL) == M:
        print(*nowL)

    for i in range(1,N+1):
        if i not in nowL and nowL[-1]<i:
            q.append(nowL + [i])





