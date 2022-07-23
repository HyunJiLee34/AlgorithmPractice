from collections import deque

dC = [-1,1,0,0]
dR = [0,0,-1,1]
L = []

q = deque([])
w = deque([])
R, C = list(map(int, input().split()))
visited = [[-1 for _ in range(C)]for _ in range(R)]
for i in range(R):
    temp = list(input())
    L.append(temp)
time = 0
def bfs():
    global time
    while q :
        nowNode = q.popleft()
        for i in range(4):
            next_R = nowNode[0]+dR[i]
            next_C = nowNode[1]+dC[i]
            if 0<=next_R<R and 0<=next_C<C :
                if L[next_R][next_C] != "*" and L[next_R][next_C] != "X" :
                    if visited[next_R][next_C]==-1:
                        visited[next_R][next_C] = visited[nowNode[0]][nowNode[1]] +1
                        time = visited[next_R][next_C]
                        q.append((next_R,next_C))
    while w :
        nowNode = w.popleft()
        for i in range(4):
            next_R = nowNode[0]+dR[i]
            next_C = nowNode[1]+dC[i]
            if 0<=next_R<R and 0<=next_C<C :
                if L[next_R][next_C] == "D" :
                    continue
                elif L[next_R][next_C] != "*" and L[next_R][next_C] != "X":
                    L[next_R][next_C] = '*'
                    w.append((next_R,next_C))

def check() :
    global time
    if visited[d[0]][d[1]]==-1:
        time = 'KAKTUS'
for i in range(R):
    for j in range(C):
        if L[i][j]=='S':
            q.append((i, j))
            visited[i][j]=0
        elif L[i][j]=='*':
            w.append((i,j))
        elif L[i][j] == 'D':
            d = [i,j]



bfs()
check()
print(time)