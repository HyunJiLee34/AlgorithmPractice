from collections import deque
n,m = map(int, input().split())
MAP = []
for i in range(n):
    temp = list(map(int,input().split()))
    MAP.append(temp)

#0 갈수 없음, 1 갈수 있음 , 2 목표지점

visited = [[0 for _ in range(m)] for _ in range(n)]
q= deque()

dR = [-1,1,0,0]
dC = [0,0,1,-1]

def bfs(startr, startc):

    q.append((startr,startc))

    while q :
        r,c  =  q.popleft()
        for i in range(4):
            nextR = r+dR[i]
            nextC = c+dC[i]
            if (0<=nextR<n  and 0<=nextC<m)  :
                if MAP[nextR][nextC]==1 and visited[nextR][nextC]==0 :
                    visited[nextR][nextC]=visited[r][c]+1
                    q.append((nextR,nextC))
    return visited

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 2 :
            ans=bfs(i,j)



for i in range(n):
    for j in range(m):
        if MAP[i][j]==1 and ans[i][j]==0 :
            ans[i][j]=-1

for i in range(n):
    print(*ans[i])

