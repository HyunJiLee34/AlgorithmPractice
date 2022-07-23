from collections import deque
N = int(input())
L = []
for i in range(N):
    temp = list(map(int, list(input().split())))
    L.append(temp)


ansL = [[0]*N for _ in range(N)]

# for i in range(N):
#     #i에서 시작해서 갈 수 있는 노드들을 구한다


def bfs(startNode):
    # visited=[0 for i in range(N)]
    q=deque([startNode])

    while(q):
        nowNode=q.popleft()

        for j in range(N):
            if L[nowNode][j] == 1 and ansL[startNode][j]==0 :
                # visited[j]=1
                ansL[startNode][j]=1
                q.append(j)

    # ansL[startNode]=list(visited)

for i in range(N):
    bfs(i)

for ans in ansL:
    print(*ans)