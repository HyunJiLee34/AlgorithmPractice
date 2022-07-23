N = int(input())
L=[]
visited = [[-1 for _ in range(N)]for _ in range(N)]
for i in range(N):
    temp = list(map(int,input().split()))
    L.append(temp)

def dfs(nowNode):
    for toNode in range(N):
        if L[nowNode][toNode]==1 and visited[nowNode][toNode]==-1:
            visited[nowNode][toNode]=1
            dfs(toNode)


for i in range(N):
    dfs(i)