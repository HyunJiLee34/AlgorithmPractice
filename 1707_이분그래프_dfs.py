import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfsf(start,group):
    global error
    visited[start]=group
    for i in D[start]:
        if error == True  : #다음 재귀함수에서 error=True인것을 골라줘야한다.
            return
        if visited[i]== 0 :
            dfsf(i,-group) #인접한 노드는 그룹을 바꿔준다.
        elif visited[start] == visited[i]:
            print("NO")
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
        if visited[i] == 0 and not error:
            dfsf(i,1)


    if not error :
        print("YES")


# import sys
# sys.setrecursionlimit(20000)
# input = sys.stdin.readline
#
# def dfsf(start, group):
#     global error
#     if error == True :
#         return
#     visited[start] = group
#     for nextnode in D[start]:
#         if visited[nextnode]==0 :
#             dfsf(nextnode,-group)
#         elif visited[nextnode] == visited[start]:
#             error = True
#             return # 재귀 빠져나옴
#
# k = int(input())
#
# for _ in range(k):
#     v,e = map(int,input().split())
#     D = {}
#     visited = [0]*(v+1)
#     error = False
#     for i in range(0,v+1):
#         D[i]=[]
#     for j in range(e):
#         a,b = map(int,input().split())
#         D[a].append(b)
#         D[b].append(a)
#
#     for i in range(1, v+1):
#         if visited[i]==0 :
#             dfsf(i,1)
#             if error == True:
#                 break
#     if error==True  :
#         print("NO")
#     else :
#         print("YES")
#
#
#



















