from collections import deque
N,L,R  = map(int, input().split())
MAP = []
q = deque([])
dR = [0,0,-1,1]
dC = [1,-1,0,0]

for i in range(N):
    temp = list(map(int, input().split()))
    MAP.append(temp)


def bfs(startr,startc):
    open_list = [(startr,startc)]
    num = MAP[startr][startc]
    visited[startr][startc]=1
    cnt = 1
    global isMove
    q.append((startr,startc))
    while q :
        r,c = q.popleft()
        for i in range(4):
            row_next = r + dR[i]
            column_next = c + dC[i]
            if (0 <= row_next < N and 0 <= column_next < N) and visited[row_next][column_next]==-1 :
                    if L<=abs(MAP[r][c]- MAP[row_next][column_next])<=R :
                        visited[row_next][column_next]=1
                        isMove =True
                        q.append((row_next,column_next))
                        cnt+=1
                        num += MAP[row_next][column_next]
                        open_list.append((row_next,column_next))

    for i,j in open_list:
        MAP[i][j]= num//cnt
ans = 0
while(1):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    isMove = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i,j)

    if isMove ==True :
        ans+=1
    else : #더이상 움직일수없으면 while 빠져나옴
        break
print(ans)


