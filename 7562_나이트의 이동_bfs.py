from collections import deque


def bfs(now_x,now_y,final_R,final_C):
    dR = [1, 2, 2, 1, -1, -2, -2, -1]
    dC = [-2, -1, 1, 2, -2, -1, 1, 2]
    q = deque([(now_x,now_y)])
    visited[now_x][now_y] = 0
    while q :
        r,c=q.popleft()
        if r == final_R and c == final_C:
            print(visited[r][c])
            return
        for i in range(8):
            next_R = r+ dR[i]
            next_C = c + dC[i]
            if 0 <= next_R < I and 0 <= next_C < I and visited[next_R][next_C] == -1:
                visited[next_R][next_C] = visited[r][c] + 1
                q.append((next_R, next_C))

T = int(input())
for i in range(T):
    I = int(input())
    visited = [[-1 for _ in range(I)] for _ in range(I)]
    now_x,now_y = list(map(int, input().split()))
    final_R,final_C = list(map(int, input().split()))
    bfs(now_x,now_y,final_R,final_C)



