from collections import deque
N = int(input())
L = []
for i in range(N):
    temp = list(map(int, list(input())))
    L.append(temp)


x_list = [0, 0, -1, 1]
y_list = [1, -1, 0, 0]
def bfsf(x,y):
    q = deque([(x, y)])
    visited[x][y]=1
    cnt = 0
    while q:
        nowNode=q.popleft()
        cnt+=1
        for i in range(4):
            x_next = nowNode[0]+x_list[i]
            y_next = nowNode[1]+y_list[i]
            if (0<=x_next<N) and (0<=y_next<N) :
                if L[x_next][y_next] == 1 and visited[x_next][y_next]==-1:
                    visited[x_next][y_next]=1
                    q.append((x_next,y_next))
    return cnt
ans_L = []
ans_c = 0
visited = [[-1 for i in range(N)]for j in range(N)]
#L=[[0]*5]*5 이렇게하면 aliasing됨
for i in range(N):
    for j in range(N):
        if L[i][j]==1 and visited[i][j]==-1:
            ans_L.append(bfsf(i,j))
            ans_c+=1
print(ans_c)
# ans_L.sort()
for i in sorted(ans_L):
    print(i)