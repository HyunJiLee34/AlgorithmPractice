from collections import deque
M,N,H = map(int,input().split())

L = [[[0 for _ in range(H)]for _ in range(M)] for _ in range(N)]

for k in range(H):
    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(M):
            L[i][j][k] = temp[j]

visited = [[[-1 for _ in range(H)]for _ in range(M)] for _ in range(N)]


dR = [-1,1,0,0,0,0]
dC = [0,0,-1,1,0,0]
dK = [0,0,0,0,1,-1]
q = deque([])
day = 0
def bfs() :
    global day
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if L[i][j][k] == 1 and visited[i][j][k] == -1:
                    visited[i][j][k] = 0
                    q.append((i,j,k))
    while q :
        nowNode = q.popleft()
        for i in range(6):
            next_R = nowNode[0]+dR[i]
            next_C = nowNode[1] + dC[i]
            next_K = nowNode[2] + dK[i]
            if 0<=next_R<N and 0<=next_C<M and 0<=next_K<H :
                if visited[next_R][next_C][next_K]==-1 and L[next_R][next_C][next_K]==0 :
                    visited[next_R][next_C][next_K] = visited[nowNode[0]][nowNode[1]][nowNode[2]] +1
                    day = visited[next_R][next_C][next_K] 
                    q.append((next_R,next_C,next_K))

def check_t():
    global day
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if visited[i][j][k]==-1 and L[i][j][k]==0 : #다 돌았는데 토마토가 익지 않고 visited되지 않았다면
                    day= -1
bfs()
check_t()
print(day)
