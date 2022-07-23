from collections import deque
N,M = map(int, input().split())
a = [list(input()) for _ in range(N)] #key
visited = [[0]*M for _ in range(N)]

def bfsf():

    visited[0][0] = 1
    q = deque([(0, 0)])
    x_list = [0, 0, -1, 1]  # 상하좌우
    y_list = [1, -1, 0, 0]  # 상하좌우
    while q :
        nowNode = q.popleft()


        for i in range(4):
            row = nowNode[0]+x_list[i]
            column = nowNode[1]+y_list[i]

            if (0<=row<N and 0<=column<M):
                if visited[row][column]==0 and a[row][column]=='1':
                    visited[row][column] = visited[nowNode[0]][nowNode[1]]+1
                    q.append((row,column))


    return visited[-1][-1]
print(bfsf())