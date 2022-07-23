import heapq
INF = 9876543210
N,D = map(int,input().split())


dist=[INF for _ in range (10001)]
dist[0]=0 #가중치
pq=[(0,0)] #가중치, 위치
graph={}
graphKeySet=set([0,D])
for i in range(N):
    S,A,short_dist = map(int,input().split())
    graphKeySet.add(S)
    graphKeySet.add(A)
    if S in graph:
        graph[S].append([A,short_dist])
    else:
        graph[S]=[[A,short_dist]]

graphKeyL=sorted(graphKeySet)
keySize=len(graphKeyL)
for i in range(keySize-1):
    diff=graphKeyL[i+1]-graphKeyL[i]
    k=graphKeyL[i]
    if k in graph:
        graph[k].append([graphKeyL[i+1],diff])
    else :
        graph[k]=[[graphKeyL[i+1],diff]]


while(pq):
    nowDist,nowNode = heapq.heappop(pq)

    if dist[nowNode]<nowDist:
        continue

    if nowNode == D :
        print(dist[D])
        break

    for toNode, toDist in graph[nowNode]:
        if toNode > D:
            continue
        addedDist = nowDist + toDist
        if addedDist < dist[toNode]:
            dist[toNode]=addedDist
            heapq.heappush(pq,(addedDist,toNode))

