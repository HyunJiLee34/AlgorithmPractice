from collections import deque
L = int(input())
originalL = []
t = 0
size = 2
cnt = 0

for i in range(L):
    temp = list(map(int,input().split()))
    originalL.append(temp)

dR = [0,0,-1,1]
dC = [1,-1,0,0]

def bfs(nowr,nowc):
    isfind = False
    q = deque([(nowr,nowc)])
    visited = [[-1 for _ in range(L)] for _ in range(L)]
    visited[nowr][nowc]=0
    candi = []
    dist=-1
    while q :
        r,c = q.popleft()
        print(r,c,isfind,dist)
        if isfind ==True :
            if visited[r][c]==dist:
                # dist가 바뀌는 순간!
                candi =sorted(candi)
                return candi
        # candi list sort, 하나 뽑기
        for i in range(4):
            nextr = r+dR[i]
            nextc = c+dC[i]

            if (0<=nextr<L) and (0<=nextc<L) and visited[nextr][nextc]==-1 and originalL[nextr][nextc] <= size:
                if originalL[nextr][nextc] ==size or originalL[nextr][nextc]==0 :
                    q.append((nextr,nextc))
                    visited[nextr][nextc]= visited[nowr][nowc]+1
                else :
                    dist = visited[nowr][nowc]+1
                    isfind = True
                    candi.append((nextr,nextc))

for i in range(L):
    for j in range(L) :
        if originalL[i][j]==9:
            print(bfs(i,j))