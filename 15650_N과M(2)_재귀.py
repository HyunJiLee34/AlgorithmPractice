N,M = map(int, input().split())

def dfsf(L):
    if len(L) == M :
        print(*L)
    for i in range(1,N+1):
        if i not in L and L[-1]<i:
            dfsf(L+[i])

for i in range(1,N+1):
    dfsf([i])




