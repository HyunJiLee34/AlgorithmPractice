from itertools import combinations
from copy import deepcopy
from collections import deque
R,C =map(int,input().split())
originalL = []
q = deque([])
for i in range(R):
    temp = list(map(int,input().split()))
    originalL.append(temp)



comb = list(combinations([i for i in range(R*C)],3))
dR = [-1,1,0,0]
dC = [0,0,-1,1]
result = 0

def bfs(): #전파 후 안전지대 개수 세기
    global result
    cnt=0
    L = deepcopy(originalL)
    for i in range(R):
        for j in range(C):
            if L[i][j] == 2:
                q.append((i, j))
    while q :
        r,c = q.popleft()
        for i in range(4):
            nextR = r+dR[i]
            nextC = c +dC[i]
            if 0 <= nextC < C and 0 <= nextR < R :
                if L[nextR][nextC] == 0:
                    L[nextR][nextC]=3
                    q.append((nextR,nextC))
    for i in range(R):
        for j in range(C):
            if L[i][j]==0:
                cnt+=1
    result = max(result,cnt)
    # for i in range(R):
    #     for j in range(L):
    #         if L[i][j]==3 :
    #             L[i][j]=0

    return result


for a, b, c in comb:
    c1 = a % C
    r1 = a // C

    c2 = b % C
    r2 = b // C

    c3 = c % C
    r3 = c // C

    if originalL[r1][c1] == 0 and originalL[r2][c2] == 0 and originalL[r3][c3] == 0:
        originalL[r1][c1] = 1
        originalL[r2][c2] = 1
        originalL[r3][c3] = 1
        bfs() #안전지대의 개수
        originalL[r1][c1] = 0
        originalL[r2][c2] = 0
        originalL[r3][c3] = 0

print(result)

#
#
#
#
#
#
#
#
#

