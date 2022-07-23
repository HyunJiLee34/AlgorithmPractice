import heapq
INF = 9876543210
graph = {}
N,M,K,X = map(int,input().split())
for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    a,b = list(map(int, input().split()))
    graph[a].append((b,1))

dist = [INF for _ in range(N+1)]
dist[X]=0
pq=[(0,X)]

while(pq):
    nowDist, nowNode=heapq.heappop(pq)
    for toNode,toDist in graph[nowNode]:
        addedDist = toDist+ nowDist
        if dist[toNode]>addedDist:
            dist[toNode]=addedDist
            heapq.heappush(pq,(addedDist,toNode))

ans_list = []
for i in range(1,N+1):
    if dist[i]==K:
        print(i)
if K not in dist:
    print(-1)



