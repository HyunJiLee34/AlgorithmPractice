from collections import deque
q = deque([])
R,C =map(int,input().split())
L = []
for i in range(R):
    temp = list(map(int,input().split()))
    L.append(temp)
dR = [-1,1,0,0]
dC = [0,0,-1,1]
virus_c = 0
def bfs():
    global virus_c
    for i in range(R):
        for j in range(C):
            if L[i][j] == 2:
                q.append((i, j))

    while q :
        r,c = q.popleft()
        for i in range(4):
            nextR = r + dR[i]
            nextC = c + dC[i]
            if 0<=nextR<R and 0<=nextC<C :
                if L[nextR][nextC]==0:
                    L[nextR][nextC]=2
                    virus_c +=1
                    q.append((nextR,nextC))
def sum():
    ans = 0
    for i in range(R):
        for j in range(C):
            if L[i][j]==0:
                ans+=1
    return ans

def wall(cnt):
    if cnt == 3 :
        bfs()
        return
    for i in range(R):
        for j in range(C):
            if L[i][j]==0:
                L[i][j]=1
                wall(cnt+1)
                L[i][j]=0
wall(0)