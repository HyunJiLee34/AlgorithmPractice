import sys
sys.setrecursionlimit(10000)
N= int(input())
MAP=[]
for i in range(N):
    temp = list(map(int, list(input())))
    MAP.append(temp)

def dfsf(startR, startC):
    visited[startR][startC] = 1
    cnt=0
    dC = [-1,1,0,0]
    dR = [0,0,-1,1]
    for i in range(4):
        next_C = startC+dC[i]
        next_R = startR +dR[i]
    if (0<=next_C<N and 0<=next_R<N) :
        if MAP[next_R][next_C] ==1 and visited[next_R][next_C]==-1:
            cnt+=1
            visited[next_R][next_C]=1
            dfsf(next_R,next_C)
    return cnt
ans_cnt = 0
ans_L = []
visited = [[-1 for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N) :
        if MAP[i][j] ==1 and visited[i][j]==-1:
            ans_L.append(dfsf(i,j))
            ans_cnt +=1
print(ans_cnt)
for i in sorted(ans_L):
    print(i)