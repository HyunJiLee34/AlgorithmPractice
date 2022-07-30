from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfsf(i,j):
    queue = deque([(i,j)])
    visited[i][j]=1
    while queue :
        r,c = queue.popleft()
        for i in range(4):
            nextr = r + dr[i]
            nextc = c + dc[i]
            if 0<=nextr<n and 0<=nextc<m:
                if visited[nextr][nextc]==-1 and MAP[nextr][nextc]==1:
                    visited[nextr][nextc] = 1
                    queue.append([nextr,nextc])
    return

t = int(input())
for _ in range(t):
    cnt = 0
    m,n,k = map(int, input().split()) #열 행
    visited = [[-1]*m for _ in range(n)]
    MAP= [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        MAP[y][x] = 1
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1 and visited[i][j]==-1:
                bfsf(i, j)
                cnt += 1

    print(cnt)


#visited를 쓰지 않은 풀이#
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfsf(i,j):
    queue = deque()
    queue.append([i,j])
    while queue :
        r,c = queue.popleft()
        for i in range(4):
            nextr = r + dr[i]
            nextc = c + dc[i]
            if 0<=nextr<n and 0<=nextc<m:
                if MAP[nextr][nextc]==1:
                    MAP[nextr][nextc]=2
                    queue.append([nextr,nextc])
    return


t = int(input())
for _ in range(t):
    cnt = 0
    m,n,k = map(int, input().split()) #열 행
    MAP = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        c,r = map(int, input().split())
        MAP[r][c]=1
    for i in range(n):
        for j in range(m):
            if MAP[i][j]==1:
                bfsf(i,j)
                cnt+=1
    print(cnt)