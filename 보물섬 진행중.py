from collections import deque
R,C = map(int,input().split())
L=[]
for i in range(R):
    temp = input()
    L.append(temp)

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]
q = deque([])
#visited = [[-1 for i in range(C)]for j in range(R)]
def bfs(startR,startC):
    q.append((startR,startC))
    visited = [[-1 for i in range(C)] for j in range(R)]
    visited[startR][startC]=0
    route = 0
    while q :
        r,c = q.popleft()
        for i in range(4):
            nextR = r +dR[i]
            nextC = c + dC[i]
            if 0<=nextR<R and 0<=nextC<C :
                if L[nextR][nextC]=='L' and visited[nextR][nextC]==-1:
                    visited[nextR][nextC] = visited[r][c]+1
                    route = visited[nextR][nextC]
                    q.append((nextR,nextC))
    return route
#for i in range(R):
    #for j in range(C):
        #if L[i][j]=='L':
            #bfs(i,j)
print(bfs(0,2))