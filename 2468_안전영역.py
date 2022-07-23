import sys
sys.setrecursionlimit(10**6)
N = int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))


dR = [-1,1,0,0]
dC = [0,0,-1,1]
visited = [[-1 for _ in range(N)] for _ in range(N)]
def dfs(startR,startC,height) :
    for i in range(4):
        next_R = startR + dR[i]
        next_C = startC + dC[i]
        if 0<=next_R<N and 0<=next_C<N :
            if L[next_R][next_C]>height and visited[next_R][next_C]==-1 :
                visited[next_R][next_C] = 1
                dfs(next_R,next_C,height)

max_list = []
for i in range(N):
    for j in range(N):
        max_list.append(L[i][j])
max_height = max(max_list)

max_cnt=0
for k in range(0, max_height+1) :
    now_cnt = 0
    visited=[[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if L[i][j]>k and visited[i][j]==-1:
                visited[i][j] = 1
                dfs(i,j,k)
                now_cnt+=1

    if now_cnt>max_cnt:
        max_cnt=now_cnt

print(max_cnt)