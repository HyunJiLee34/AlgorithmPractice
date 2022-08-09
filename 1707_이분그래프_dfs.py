import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfsf(start,group):
    global error
    if error :
        return
    visited[start]=group
    for i in D[start]:
        if visited[i]== 0 :
            dfsf(i,-group) #인접한 노드는 그룹을 바꿔준다.
        elif visited[start] == visited[i]:
            error=True
            return #재귀리턴





k = int(input())
for _ in range(k): #test case 시작
    v,e = map(int, input().split())
    D = [[]for i in range(v+1)]
    visited = [0] * (v + 1)
    error = False
    for _ in range(e):
        u, v = map(int, input().split())
        D[u].append(v)
        D[v].append(u)

    for i in range(1,v+1):
        if visited[i] == 0 :
            dfsf(i,1)
            if error==True :
                break #for문나옴
    if error  :
        print("NO")
    else :
        print("YES")

