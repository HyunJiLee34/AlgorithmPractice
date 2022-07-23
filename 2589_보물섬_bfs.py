from collections import deque
R,C = map(int, input().split())
L=[]
q = deque([])
visited = [[-1 for _ in range(C)] for _ in range(R)]


for i in range(R):
    temp = input()
    L.append(temp)

def bfs(startR,startC):
    visited = [[-1 for a in range(C)]for b in range(R)]
    visited[startR][startC]=0
    q = deque([(startR,startC)])
    route = 0
    dR = [-1, 1, 0, 0]
    dC = [0, 0, -1, 1]
    while q:
        r,c = q.popleft()

        for i in range(4):
            nextR = r + dR[i]
            nextC = c + dC[i]
            if 0<=nextR<R and 0<=nextC<C :
                if L[nextR][nextC]=='L' and visited[nextR][nextC]==-1:
                    visited[nextR][nextC] = visited[r][c]+1
                    route = visited[nextR][nextC]
                    q.append((nextR,nextC))
    return route

path_list = []

for i in range(R):
    for j in range(C):
        if L[i][j]=='L' :
            path_list.append(bfs(i,j))
print(max(path_list))


