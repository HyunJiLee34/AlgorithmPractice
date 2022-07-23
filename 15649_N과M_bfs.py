from collections import deque
N,M = map(int, input().split())
q = deque([])
for i in range(1,N+1):
    q.append([i])
while q:
    nowL = q.popleft()
    if len(nowL)==M:
        print(*nowL)
    for i in range(1,N+1):
        if i in nowL :
            continue
        else :
            q.append(nowL+[i])