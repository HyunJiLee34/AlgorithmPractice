import sys
sys.setrecursionlimit(10000)
N = int(input())
L = []
for i in range(N):
    temp = list(input())
    L.append(temp)

dC = [-1,1,0,0]
dR = [0,0,-1,1]
cnt = 0
visited= [[-1 for _ in range(N)] for _ in range(N)]

def dfsf(startR, startC, type):
    for i in range(4):
        nextR = startR+dR[i]
        nextC = startC+dC[i]
        if 0<=nextR<N and 0<=nextC<N :
            nextColor = L[nextR][nextC]
            if nextColor in type and visited[nextR][nextC]==-1:
                visited[nextR][nextC]=1
                dfsf(nextR, nextC, type)



for i in range(N):
    for j in range(N):
        if (L[i][j]=='R' or L[i][j]=='G') and visited[i][j]==-1 :
            visited[i][j] = 1
            dfsf(i,j,['R','G'])
            cnt+=1
        elif (L[i][j]=='B') and visited[i][j]==-1:
            visited[i][j]=1
            dfsf(i,j,'B')
            cnt+=1
visited= [[-1 for _ in range(N)] for _ in range(N)] #초기화
non_cnt = 0
for i in range(N):
    for j in range(N):
        if L[i][j]=='R' and visited[i][j]==-1 :
            visited[i][j]=1
            dfsf(i,j,'R')
            non_cnt += 1
        elif (L[i][j]=='B') and visited[i][j]==-1:
            visited[i][j]=1
            dfsf(i,j,'B')
            non_cnt += 1
        elif L[i][j]=='G' and visited[i][j]==-1 :
            visited[i][j]=1
            dfsf(i,j,'G')
            non_cnt+=1
print(non_cnt,cnt)
