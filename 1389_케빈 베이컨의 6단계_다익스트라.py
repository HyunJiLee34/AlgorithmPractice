import heapq
N,M = map(int, input().split())
graph = {}
for i in range(1,N+1):
    graph[i]=[]
for i in range(M):
    f1,f2 = map(int, input().split())
    graph[f1].append([f2,1])
    graph[f2].append([f1, 1])
INF = 9876543210
dist = [INF for i in range(N+1)]
dist[1]=0
print(graph)
ans_L = []
for i in range(1,N+1):
    pq = [(0,k)]
    while(pq):
        nowDist, nowNode = heapq.heappop(pq)
        if dist[nowNode]<nowDist:
            continue
        for toNode,toDist in graph[nowNode]:
            addedDist = nowDist + toDist
            if dist[toNode]>addedDist :
                dist[toNode]=addedDist
                print(dist[toNode])
                heapq.heappush(pq,(addedDist,toNode))
    ans_L.append(())
    print(dist)











