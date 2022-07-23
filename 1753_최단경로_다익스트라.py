import heapq
INF=9876543210

V,E=map(int,input().split())
S=int(input())

graph={}
for _ in range(1,V+1):
    graph[_]=[]

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])

dist=[INF for _ in range(V+1)]
dist[S]=0
pq=[(0,S)]

while(pq):
    nowDist,nowNode=heapq.heappop(pq)

    if dist[nowNode]<nowDist:
        continue
    for toNode,addW in graph[nowNode]:
        addedDist=addW+nowDist
        if addedDist<dist[toNode]:
            dist[toNode]=addedDist
            heapq.heappush(pq,(addedDist,toNode))
            print(pq)

for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])