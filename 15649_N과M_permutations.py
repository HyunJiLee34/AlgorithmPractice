from itertools import permutations

N,M = map(int, input().split())
L = [i for i in range(1,N+1)]
for t in list(permutations(L,M)):
    print(*t)