from collections import deque
w,h = map(int, input().split())
MAP = [[0 for _ in range(w+2)] for i in range(h+2)] #가로 세로 +2
for i in range(1,h+1):
    MAP[i][1:w+1] = map(int, input().split())

dR = []
visited = [[-1 for _ in range(w+2)] for i in range(h+2)]




odd_r = [-1, 1, 0, 0, 1, -1]  # 홀수행 위, 아래, 왼쪽, 오른쪽, 오른쪽아래, 오른쪽위
odd_c = [0, 0, -1, 1, 1, 1]  # 홀수열

even_r = [-1, 1, 0, 0, 1, -1]  # 홀수행 위, 아래, 왼쪽, 오른쪽, 왼쪽아래, 왼쪽위
even_c = [0, 0, -1, 1, -1, -1]  # 홀수열
q = deque()




def bfs(row,column):
    cnt= 0
    q.append((row, column))
    visited[row][column] = 0
    while q :
        r,c = q.popleft()
        if r %2 == 0:
            for i in range(6):
                nR = r+even_r[i]
                nC = c + even_c[i]
                if 0<=nR<h+2 and 0<=nC<w+2:
                    if visited[nR][nC] == -1 and MAP[nR][nC]==1 :
                        cnt+=1
                    elif visited[nR][nC]==-1 and MAP[nR][nC]==0:
                        q.append((nR, nC))
                        visited[nR][nC]=0


        else :
            for i in range(6):
                nR = r+odd_r[i]
                nC = c +odd_c[i]
                if 0<=nR<h+2 and 0<=nC<w+2:
                    if visited[nR][nC] == -1 and MAP[nR][nC]==1 :
                        cnt+=1
                    elif visited[nR][nC] == -1 and MAP[nR][nC] == 0:
                        q.append((nR, nC))
                        visited[nR][nC] = 0
    return cnt


print(bfs(0,0))
