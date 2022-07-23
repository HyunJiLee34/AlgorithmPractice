# import sys
# sys.setrecursionlimit(10000)
#
# def dfsf(startr,startcol):
#     dC = [-1, 1, 0, 0, 1, -1, 1, -1]
#     dL = [0, 0, -1, 1, 1, -1, -1, 1]
#     for k in range(8):
#         nextC = startcol+dC[k]
#         nextR = startr +dL[k]
#         if 0<=nextC<w and 0<=nextR<h :
#             if L[nextR][nextC]==1:
#                 L[startr][startcol]=0
#                 L[nextR][nextC]=0
#                 dfsf(nextR,nextC)
#
# while True :
#     w,h = map(int, input().split())
#     L=[]
#     cnt=0
#     for i in range(h):
#         temp = list(map(int,input().split()))
#         L.append(temp)
#     for i in range(h):
#         for j in range(w):
#             if L[i][j]==1:
#                 dfsf(i,j)
#                 cnt+=1
#     print(cnt)

