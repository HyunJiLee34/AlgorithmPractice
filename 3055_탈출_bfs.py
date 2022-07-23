from collections import deque
import sys

dR=[0,0,-1,1]
dC=[-1,1,0,0]

R,C=map(int,input().split())
L=[]
for i in range(R):
    L.append(list(input()))

def water():
    A=[]
    for i in range(R):
        for j in range(C):
            if L[i][j]=="*":
                A.append([i,j]) #물의 위치
    for r,c in A: #물이 있는 곳에서 좌우상하에 "1회" 물넘침
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<R and 0<=tempC<C :
                if L[tempR][tempC]=='.':
                    L[tempR][tempC]="*"

q=deque([])
visited=[[-1 for j in range(C)] for i in range(R)]
for i in range(R):
    for j in range(C):
        if L[i][j]=="S":
            q.append([i,j])
            visited[i][j]=0

def dotch():
    size=len(q)
    ismoved = False
    for i in range(size):
        r, c = q.popleft()
        for k in range(4):  # 고슴도치 움직이기
            tempR = r + dR[k]
            tempC = c + dC[k]
            if 0 <= tempR < R and 0 <= tempC < C and L[tempR][tempC] in [".", "D"] and visited[tempR][tempC]==-1:
                if L[tempR][tempC] == ".":  # 인도면 이동
                    q.append([tempR, tempC])
                    visited[tempR][tempC] = visited[r][c] + 1
                    ismoved=True
                elif L[tempR][tempC] == "D" :  # 비버집이면 끝!
                    return visited[r][c] + 1

    if ismoved ==True: #아직가야할길이있음
        return -1
    else :
        return 'KAKTUS'
while(1):
    water()
    a=dotch()
    if a ==-1 :
        continue
    else :
        print(a)
        break