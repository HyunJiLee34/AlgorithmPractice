from collections import deque
N,M = map(int, input().split())
L = []
for i in range(N):
    L.append(input())
visited = [[[-1 for _ in range(2)] for _ in range(M)]for _ in range(N)]

dR = [-1,1,0,0]
dC = [0,0,1,-1]


def bfsf(startR,startC,floor):
    q = deque([(startR,startC,floor)])
    visited[startR][startC][floor]=1
    while q :
        nowNode = q.popleft()
        floor = nowNode[2]
        for i in range(4):
            next_R = nowNode[0] + dR[i]
            next_C = nowNode[1] + dC[i]
            if 0 <= next_R < N and 0 <= next_C < M:
                if L[next_R][next_C] == '0' :
                    if visited[next_R][next_C][floor] == -1 :
                        visited[next_R][next_C][floor] = visited[nowNode[0]][nowNode[1]][floor]+1
                        q.append((next_R,next_C,floor))
                elif L[next_R][next_C] == '1' :
                    if floor == 0 :
                        if visited[next_R][next_C][floor] == -1 :
                            visited[next_R][next_C][1] = visited[nowNode[0]][nowNode[1]][floor] + 1
                            q.append((next_R, next_C,1))

bfsf(0,0,0)
# if N ==1 and M ==1 :
#     if L[N-1][M-1] =='1':
#         print(-1)
#     elif L[N-1][M-1] =='0':
#         print(1)
if visited[N-1][M-1][1] == -1 and visited[N-1][M-1][0]==-1:
    print(-1)
elif visited[N-1][M-1][0]==-1:
    print(visited[N-1][M-1][1])
elif visited[N-1][M-1][1] == -1 :
    print(visited[N-1][M-1][0])
else:
    print(min(visited[N-1][M-1]))
