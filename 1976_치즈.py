from collections import deque
import sys

L = []
preC=0

R,C = map(int,input().split())
for i in range(R):
    temp = list(map(int,input().split()))
    L.append(temp)

def frame_bfs():
    visited = [[-1 for i in range(C)] for j in range(R)]
    q = deque([(0, 0)])
    visited[0][0]=1
    dR = [-1, 1, 0, 0]
    dC = [0, 0, -1, 1]
    while q :
        r,c = q.popleft()
         #이미 nextr nextC에서 1 처리해주지 않나?
        for i in range(4):
            next_R = r+dR[i]
            next_C = c + dC[i]
            if 0<=next_R<R and 0<=next_C<C and visited[next_R][next_C]==-1:
                if L[next_R][next_C]==0:
                    visited[next_R][next_C]=1
                    q.append((next_R,next_C))
                elif L[next_R][next_C]==1:
                    visited[next_R][next_C]=1
                    L[next_R][next_C]=2

def melt():
    global preC
    for i in range(R):
        for j in range(C):
            if L[i][j]==2:
                L[i][j]=0

def isCheese():
    for i in range(R):
        for j in range(C):
            if L[i][j]==1:
                return True
    else :
        return False

def cntC():
    a=0
    for i in range(R):
        for j in range(C):
            if L[i][j]==1:
                a+=1
    return a

cnt = 1
preC=cntC()
while(1):
    frame_bfs()
    melt()

    if not isCheese():
        print(cnt)
        print(preC)
        break
    else:
        cnt+=1
        preC=cntC()











