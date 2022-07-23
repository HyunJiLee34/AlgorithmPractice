from collections import deque
N = int(input())
L = []
for i in range(N):
    temp = list(map(int, list(input().split())))
    L.append(temp)



def dfs(nowNode):
    for toNode in range(N):
        if L[nowNode][toNode]==1 and visited[toNode] ==0:
            visited[toNode]=1
            dfs(toNode)


#함수는 inplace=True역할을 한다 (단, 숫자제외), visited는 dfs함수를 통해 계속 갱신이되기 떄문에
#출력을 할 때 갱신된 visited가 찍히는것


for i in range(N):
    visited = [0 for i in range(N)] #0에서 1로 갈수있고 1이 3으로 갈수 있으면 0의 visited에 0이 3으로 갈 수있는것도 표시함
    dfs(i)
    print(*visited)