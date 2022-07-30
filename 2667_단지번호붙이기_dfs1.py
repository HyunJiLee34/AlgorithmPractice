N = int(input())
L=[]
v = 1
visited = [[-1 for _ in range(N)]for i in range(N)]

for i in range(N):
    temp=list(map(int,input()))
    L.append(temp)
def dfs(x,y):
    global v, visited,cnt
    visited[x][y]= 1
    dc = [-1,1,0,0]
    dr = [0,0,-1,1]
    for i in range(4):
        nextR = x+dr[i]
        nextC = y+dc[i]
        if 0 <= nextR < N and 0 <= nextC < N:
            if visited[nextR][nextC]==-1 and L[nextR][nextC]==1:
                visited[nextR][nextC]=1
                cnt+=1
                dfs(nextR,nextC)
    return cnt
vcnt=0
ansL=[]
for i in range(N):
    for j in range(N):
        if L[i][j]==1 and visited[i][j]==-1:
            cnt=1
            ansL.append(dfs(i,j))
            vcnt+=1
print(vcnt)
for i in sorted(ansL):
    print(i)