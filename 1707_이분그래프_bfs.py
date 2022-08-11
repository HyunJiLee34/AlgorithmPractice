import sys
from collections import deque
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def bfsf(start):
    global error
    visited[start] = 1
    while q:
        nownode = q.popleft() #큐의 맨앞 원소 빼낸다
        for j in D[nownode]: #해당 점점에서 갈 수 있는 하위 정점들을 돈다.
            if visited[j]==0 : #만약 아직 방문하지 않았다면
                q.append(j) #큐에 정점을 추가하고
                visited[j]= -1 * visited[nownode] #상반된 그룹에 편성한다.
                print(visited)
            elif visited[j] == visited[nownode]: #만약 방문하였는데 같은 그룹이라면
                print("NO") #NO를 출력하고
                error = True #error로 바꾸고
                return #함수 나가기


k = int(input())
for _ in range(k): #test case 시작
    v,e = map(int, input().split())
    D = [[]for i in range(v+1)]
    visited = [0] * (v + 1)
    q = deque()
    error = False
    for _ in range(e):
        u, v = map(int, input().split())
        D[u].append(v)
        D[v].append(u)

    for i in range(1,v+1):
        if visited[i] == 0 and not error:
            q.append(i)
            bfsf(i)

    if error ==False :
        print("YES")