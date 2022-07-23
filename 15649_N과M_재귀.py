from collections import deque
N,M = map(int, input().split())
def bfsf(L):
    if len(L)==M:
        print(*L)
    for i in range(1,N+1):
        if i in L:
            continue
        else :
            bfsf(L+[i])

bfsf([])

