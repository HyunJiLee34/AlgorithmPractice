from collections import deque
n,m = map(int, input().split()) #사다리수 , 뱀수
graph = {}

for i in range(n+m):
    x,y = map(int,input().split()) #x도착하면 y로 이동 #사다리,뱀
    graph[x]=y


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
                if nextnode in graph.keys():
                    nextnew = graph[nextnode]
                    if visited[nextnew]==0 :
                        visited[nextnew] = visited[nownode]+1
                        q.append(nextnew)
                else :
                    q.append(nextnode)

bfsf()

