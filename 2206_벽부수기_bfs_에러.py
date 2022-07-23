from collections import deque
N,M = map(int, input().split())
L = []
for i in range(N):
    L.append(input())
visited = [[[-1 for _ in range(2)] for _ in range(M) for _ in range(N)]]
q = deque([(0,0,0)])
dC = [-1,1,0,0]
dR= [0,0,-1,1]
visited[0][0][0]=1
while q :
    nowNode= q.popleft()
    floor = nowNode[2]

    for i in range(4):
        next_R = nowNode[0]+dR[i]
        next_C = nowNode[1] + dC[i]
        if 0 <= next_R < N and 0 <= next_C < M:
            if L[next_R][next_C] == '0':
                if visited[next_R][next_C][floor]==-1:
                    visited[next_R][next_C][floor] = visited[nowNode[0]][nowNode[1]][floor]+1
                    q.append([(next_R,next_C,floor)])
            elif L[next_R][next_C] == '1' :
                if floor == 0:
                    if visited[next_R][next_C][floor] == -1:
                        visited[next_R][next_C][1] = visited[nowNode[0]][nowNode[1]][floor]+1
                        q.append([(next_R,next_C,1)])

# if visited[N-1][M-1][1]==-1 and visited[N-1][M-1][0]==-1:
#     print(-1)
# elif visited[N-1][M-1][1]==-1:
#     print(visited[N-1][M-1][0])
# elif visited[N-1][M-1][0]==-1:
#     print(visited[N - 1][M - 1][1])
# else :
#     print(min(visited[N-1][M-1]))#0층이랑 1층 두경우가 모두나오는것인가? bfs여서 가능? 경우의 수 여러개가 append되어서?