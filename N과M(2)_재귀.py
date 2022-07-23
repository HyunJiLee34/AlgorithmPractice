from collections import deque
import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
q = deque([])

visited = [-1 for _ in range(N+1)]

def bfsf(L):
    
    for i in range(1, N + 1):
        bfsf(L+[i])
