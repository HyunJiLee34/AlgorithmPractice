import sys
sys.setrecursionlimit(10000)
M,N,K = map(int, input().split()) # M은 row N은 column
L=[]
MAP = [[0 for _ in range(N)]for _ in range(M)]

for i in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            MAP[j][k]=1

dC = [-1,1,0,0]
dR = [0,0,-1,1]
visited = [[-1 for _ in range(N)]for _ in range(M)]
def dfsf(startR, startC):
    global cnt
    for i in range(4):
        nextR = startR + dR[i]
        nextC = startC + dC[i]
        if 0<=nextR<M and 0<=nextC<N :
            if visited[nextR][nextC]==-1 and MAP[nextR][nextC]==0:
                visited[nextR][nextC]=1
                cnt+=1
                dfsf(nextR,nextC)
    return cnt

ans_list=[]
cnt =0
for a in range(M):
    for b in range(N):
        if MAP[a][b] ==0 and visited[a][b]==-1 :
            visited[a][b]=1
            cnt=1
            ans_list.append(dfsf(a, b))
print(len(ans_list))
print(*sorted(ans_list))

#


