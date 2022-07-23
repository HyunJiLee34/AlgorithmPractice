from collections import deque
day = 0
L = []
N,M = map(int, input().split())
for i in range(M):
    temp = list(map(int, list(input().split())))
    L.append(temp)

dR = [0,0,-1,1]
dC = [1,-1,0,0]
q = deque([])
visited = [[-1 for _ in range(N)] for _ in range(M)]


def bfs():
    global day
    for i in range(M):
        for j in range(N):
            if L[i][j] == 1:
                visited[i][j]=0
                q.append((i, j))

    while q:
        nowNode = q.popleft()
        for i in range(4):
            row_next = nowNode[0]+dR[i]
            column_next = nowNode[1]+dC[i]
            if (0<=row_next<M and 0<=column_next<N):
                if L[row_next][column_next]==0 and visited[row_next][column_next]==-1:
                    visited[row_next][column_next]=visited[nowNode[0]][nowNode[1]]+1
                    day= visited[row_next][column_next]
                    q.append((row_next,column_next))

def check_t():
    global day
    for i in range(M):
        for j in range(N):
            if visited[i][j]==-1 and L[i][j]==0 :
                day= -1

bfs()
check_t()

print(day)
