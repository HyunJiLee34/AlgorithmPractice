import heapq
INF=9876543210


num_city=int(input())
num_bus = int(input())

graph={}
for _ in range(1,num_city+1):
    graph[_]=[]

for _ in range(num_bus):
    a,b,f=map(int,input().split())
    graph[a].append([b,f])
S,A = map(int,input().split())

dist=[INF for _ in range(num_city+1)]
dist[S]=0
pq=[(0,S)]

while(pq):
    nowDist,nowNode=heapq.heappop(pq)

    if dist[nowNode]<nowDist:
        continue

    if nowNode == A :
        print(nowDist)
        break

    for toNode,addW in graph[nowNode]:
        addedDist=addW+nowDist

        if addedDist<dist[toNode]:
            dist[toNode]=addedDist
            heapq.heappush(pq,(addedDist,toNode))