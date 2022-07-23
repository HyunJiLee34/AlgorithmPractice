from collections import deque
R,C = map(int, input().split())
L=[]
preC=0
for i in range(R):
    temp = list(map(int,input().split()))
    L.append(temp)
dC = [-1,1,0,0]
dR = [0,0,-1,1]

q = deque([(0,0)])
visited= [[-1 for i in range(C)]for j in range(R)]
visited[0][0]=1

def frame_bfs():
    while q :
        r, c = q.popleft()
        for i in range(4):
            next_r = r + dR[i]
            next_c = c + dC[i]
            if 0<=next_r<R and 0<=next_c<C :
                if visited[next_r][next_c]==-1 and L[r][c]==1:
                    L[next_r][next_c]=2
                    visited[next_r][next_c]=1
                elif visited[next_r][next_c]==-1 and L[r][c]==0:
                    visited[next_r][next_c]=1
                    q.append((next_r,next_c))

def melt():
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

cnt=1
preC = cntC()
while(1):
    frame_bfs()
    melt()

    if not isCheese():
        print(cnt)
        print(preC)
        break
    else :
        cnt+=1
        preC = cntC()