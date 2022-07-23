
M, N = map(int, input().split())
MAP= []

visited = [[0 for _ in range(N)]for _ in range(M)]

for i in range(M):
    temp = input().split()
    MAP.append(temp)

dR = [-1,1,0,0]
dC = [0,0,-1,1]


visited[0][0]=1

cnt=0
def dfs(startR,startC):
    global cnt
    if startR == M-1 and startC == N-1 :
        cnt+=1 #다른경로들은??
    for i in range(4):
        nextR = startR+dR[i]
        nextC = startC + dC[i]
        if 0<=nextR<M and 0<=nextC<N:
            if MAP[nextR][nextC]<MAP[startR][startC] and visited[nextR][nextC]==0:
                visited[nextR][nextC]=1
                dfs(nextR,nextC)
                visited[nextR][nextC]=0

dfs(0,0)
print(cnt)