from collections import deque
N,M, T = map(int, input().split())
MAP = []
for i in range(N):
    temp = list(map(int, input().split()))
    MAP.append(temp)
#0은 빈공간, 1은 마법의 벽, 2는 그람
#N,M 은 공주의 위치
#용사가 들어가는 곳 (0,0)은 (1,1)로 간주
# T시간 혹은 T시간 안에 들어가야함
#한칸 이동하는데에 1시간걸림
#최단시간 - bfs
dR = [-1,1,0,0]
dC = [0,0,-1,1]

visited = [[-1 for _ in range(M)] for _ in range(N)]
result = float('inf')

def bfsf(startr,startc,time) :
    global visited, result
    q = deque()
    q.append((startr,startc,time))
    visited[startr][startc]=1
    while q :
        r,c,t= q.popleft()
        if r == N-1 and c == M-1 :
            result = min(result, t)
            break
        if t > T :
            break
        for i in range(4):
            nextR = r + dR[i]
            nextC = c + dC[i]
            if (0<=nextR<N and 0<=nextC<M) and visited[nextR][nextC]==-1 :
                if MAP[nextR][nextC]==0:
                    visited[nextR][nextC]=1
                    q.append((nextR,nextC,t+1)) #걸리는 시간비교를 위해 t도 q에 넣음
                elif MAP[nextR][nextC]==2 : #그람 찾음 #벽부수기 가능
                    visited[nextR][nextC]=1
                    tmp = t +1 + abs((N-1)-nextR)+abs((M-1)-nextC)
                    if tmp <=T :
                        result = tmp



bfsf(0,0,0)

if result>T :
    print("Fail")
else :
    print(result)