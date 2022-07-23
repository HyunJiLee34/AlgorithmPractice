
from collections import deque

def bfsf(startr,startcol):
    dC = [-1, 1, 0, 0, 1, -1, 1, -1]
    dR = [0, 0, -1, 1, 1, -1, -1, 1]
    q = deque([])
    q.append((startr,startcol))
    while q :
        nowNode = q.popleft()
        for k in range(8):
            nextC = nowNode[1] + dR[k]
            nextR = nowNode[0] + dC[k]
            if 0<=nextC<w and 0<=nextR<h :
                if L[nextR][nextC]==1:
                    L[startr][startcol]=0
                    L[nextR][nextC]=0
                    q.append((nextR,nextC))

while True :
    w,h = map(int, input().split())
    if (w,h)==(0,0):
        break
    L=[]
    cnt=0
    for i in range(h):
        temp = list(map(int,input().split()))
        L.append(temp)
    for i in range(h):
        for j in range(w):
            if L[i][j]==1:
                bfsf(i,j)
                cnt+=1
    print(cnt)