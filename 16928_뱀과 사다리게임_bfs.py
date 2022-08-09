from collections import deque
n,m = map(int, input().split()) #사다리수 , 뱀수
ladder = {}
snake = {}

for i in range(n):
    x,y = map(int,input().split()) #x도착하면 y로 이동 #사다리
    ladder[x]=y
for j in range(m):
    a,b = map(int, input().split()) #뱀
    snake[a]=b

visited = [0]*101



def bfsf():
    q = deque()
    q.append(1)
    while q :
        nownode = q.popleft()
        if nownode == 100:
            print(visited[nownode])
            return
        for i in range(1,7):
            nextnode = nownode+i
            if 0<nextnode<=100 and visited[nextnode]==0:
                visited[nextnode]=visited[nownode]+1
                #사다리가 있는경우
                if nextnode in ladder.keys():
                    nextladder = ladder[nextnode]
                    if visited[nextladder]==0 :
                        visited[nextladder] = visited[nownode]+1
                        q.append(nextladder)

                elif nextnode in snake.keys():
                    nextsnake = snake[nextnode]
                    if visited[nextsnake]==0:
                        visited[nextsnake] = visited[nownode] + 1
                        q.append(nextsnake)
                else :
                    q.append(nextnode)

bfsf()

