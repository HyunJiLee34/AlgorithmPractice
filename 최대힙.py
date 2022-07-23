import heapq
import sys

N= int(input())
pq=[]

for i in range(N):
    X=int(sys.stdin.readline())*-1
    if X==0:
        if not pq:
            print(0)
        else:
            min_val = heapq.heappop(pq)
            # min_val = min(L)
            # L.remove(min_val)
            print(min_val*-1)
    else:
        heapq.heappush(pq,X)
        # L.append(X)