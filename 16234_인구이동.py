# from collections import deque
# N,L,R  = map(int, input().split())
# MAP = []
# q = deque([])
# dR = [0,0,-1,1]
# dC = [1,-1,0,0]
#
# for i in range(N):
#     temp = list(map(int, input().split()))
#     MAP.append(temp)
#
#
# def bfs(startr,startc):
#     open_list = [(startr,startc)]
#     num = MAP[startr][startc]
#     visited[startr][startc]=1
#     cnt = 1
#     global isMove
#     q.append((startr,startc))
#     while q :
#         r,c = q.popleft()
#         for i in range(4):
#             row_next = r + dR[i]
#             column_next = c + dC[i]
#             if (0 <= row_next < N and 0 <= column_next < N) and visited[row_next][column_next]==-1 :
#                     if L<=abs(MAP[r][c]- MAP[row_next][column_next])<=R :
#                         visited[row_next][column_next]=1
#                         isMove =True
#                         q.append((row_next,column_next))
#                         cnt+=1
#                         num += MAP[row_next][column_next]
#                         open_list.append((row_next,column_next))
#
#     for i,j in open_list:
#         MAP[i][j]= num//cnt
# ans = 0
# while(1):
#     visited = [[-1 for _ in range(N)] for _ in range(N)]
#     isMove = False
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == -1:
#                 bfs(i,j)
#
#     if isMove ==True :
#         ans+=1
#     else : #더이상 움직일수없으면 while 빠져나옴
#         break
# print(ans)
#
#
from collections import deque
N,L,R = map(int, input().split())
MAP = []
for i in range(N):
    num = list(map(int, input().split()))
    MAP.append(num)

q= deque()

def bfs(startr,startc):
    global ismove
    q.append((startr,startc))
    cnt=1 #국가 수 카운트
    num = MAP[startr][startc]  # 인구수 카운트
    nation = [(startr,startc)]
    visited[startr][startc]=1
    dR = [-1,1,0,0]
    dC = [0,0,-1,1]
    while q :
        r,c = q.popleft()
        for i in range(4):
            nextR = r + dR[i]
            nextC = c + dC[i]

            if (0<=nextR<N and 0<=nextC<N) and visited[nextR][nextC]==-1 :
                    # 인구차이가 L과 R사이라면 국경엶
                    if L<=abs(MAP[r][c]-MAP[nextR][nextC])<=R :
                        ismove=True
                        visited[nextR][nextC]=1
                        cnt += 1
                        q.append((nextR,nextC))
                        num += MAP[nextR][nextC]
                        nation.append((nextR, nextC))

    # 국가마다 인구수를 변경해줘야함
    for a,b in nation :
        MAP[a][b]= num//cnt

# 연합이 가능할때까지 반복해야하기 때문에 while문
ans =0
while(1) :
    visited = [[-1 for _ in range(N)] for _ in range(N)] #새로운 while문 돌때마다 visited 갱신필요
    ismove =False
    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1 :
                bfs(i,j) #bfs 한번 끝낼때마다 ans+=1
    if ismove == True :
        ans+=1
    else :  #더이상 인구이동이 불가능하면 while 문에서 빠져나옴
        break


print(ans)























