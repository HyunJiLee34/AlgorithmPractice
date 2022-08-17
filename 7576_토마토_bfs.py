# from collections import deque
# day = 0
# L = []
# N,M = map(int, input().split())
# for i in range(M):
#     temp = list(map(int, list(input().split())))
#     L.append(temp)
#
# dR = [0,0,-1,1]
# dC = [1,-1,0,0]
# q = deque([])
# visited = [[-1 for _ in range(N)] for _ in range(M)]
#
#
# def bfs():
#     global day
#     for i in range(M):
#         for j in range(N):
#             if L[i][j] == 1:
#                 visited[i][j]=0
#                 q.append((i, j))
#
#     while q:
#         nowNode = q.popleft()
#         for i in range(4):
#             row_next = nowNode[0]+dR[i]
#             column_next = nowNode[1]+dC[i]
#             if (0<=row_next<M and 0<=column_next<N):
#                 if L[row_next][column_next]==0 and visited[row_next][column_next]==-1:
#                     visited[row_next][column_next]=visited[nowNode[0]][nowNode[1]]+1
#                     day= visited[row_next][column_next]
#                     q.append((row_next,column_next))
#
# def check_t():
#     global day
#     for i in range(M):
#         for j in range(N):
#             if visited[i][j]==-1 and L[i][j]==0 :
#                 day= -1
#
# bfs()
# check_t()
#
# print(day)































from collections import deque
q = deque()
m,n = map(int, input().split())
MAP = []
day = 0
visited = [[-1 for _ in range(m)] for k in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    MAP.append(temp)


dR = [-1,1,0,0]
dC = [0,0,-1,1]


for i in range(n):
    for j in range(m):
        if MAP[i][j]==1 and visited[i][j]==-1:
            visited[i][j]=0
            q.append((i,j))
while q :
    r,c = q.popleft()
    for k in range(4):
        nR = r+dR[k]
        nC = c + dC[k]
        if 0<=nR<n and 0<=nC<m :
            if MAP[nR][nC] == 0 and visited[nR][nC]==-1 :
                visited[nR][nC] = visited[r][c]+1
                day = visited[nR][nC] #누적된날짜
                q.append((nR,nC))

for i in range(n):
    for j in range(m):
        if MAP[i][j]==0 and visited[i][j]==-1:
            day = -1
print(day)
