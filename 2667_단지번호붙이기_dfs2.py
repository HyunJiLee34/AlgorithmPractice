n = int(input())
MAP = []
for i in range(n):
    tmp = list(map(int,input()))
    MAP.append(tmp)
visited = [[-1for _ in range(n)] for i in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]


#단지 내 집개수 카운트

def dfsf(r,c):
    global tmp, visited, tmp
    visited[r][c] = 1
    for i in range(4):
        nextr= r+dr[i]
        nextc= c+dc[i]
        if 0 <= nextr < n and 0 <= nextc < n and visited[nextr][nextc] == -1:
            if MAP[nextr][nextc] == 1:
                tmp+=1
                dfsf(nextr,nextc)
    return tmp


anscnt=0
ansL = []
for i in range(n):
    for j in range(n):
        if MAP[i][j] ==1 and visited[i][j]==-1:
            tmp = 1
            ansL.append(dfsf(i,j))
            anscnt+=1

print(anscnt)
for i in sorted(ansL) :
    print(i)
