

import sys
sys.setrecursionlimit(10000)



def dfsf(startr,startcol):
    dR = [0, 0, -1, 1]
    dC = [1, -1, 0, 0]
    for i in range(4):
        row_next = startr+dR[i]
        column_next = startcol+dC[i]
        if (0<=row_next<M and 0<=column_next<N):
            if MAP[row_next][column_next]==1 :
                MAP[startr][startcol]=0
                MAP[row_next][column_next]=0
                dfsf(row_next,column_next)

T = int(input())
for _ in range(T):
    cnt = 0
    M,N,K = map(int, input().split())
    MAP = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        MAP[x][y]=1
    for i in range(M):
        for j in range(N):
            if MAP[i][j]==1:
                dfsf(i,j)
                cnt+=1
    print(cnt)
#
#



# ansL = [[0]*N for _ in range(N)]

# for i in range(N):
#     #i에서 시작해서 갈 수 있는 노드들을 구한다

















