import heapq
INF = 9876543210
N,K = map(int,input().split())

INF = 9876543210
dist=[INF for _ in range (100001)]
dist[N]=0 #가중치
pq=[(0,N)] #가중치, 위치
while (pq):
    nowDist, nowNode=heapq.heappop(pq)
    if dist[nowNode]<nowDist:
        continue

    if nowNode == K :
        print(dist[K])
        break

    # X-1
    if nowNode-1>=0 and dist[nowNode-1] > nowDist+1 :
        dist[nowNode-1]=nowDist+1
        heapq.heappush(pq,(nowDist+1,nowNode-1))

    #x+1
    if nowNode+1 < 100001 and dist[nowNode+1] > nowDist+1:
        dist[nowNode+1]=nowDist+1
        heapq.heappush(pq,(nowDist+1,nowNode+1))

    #순간이동
    if nowNode*2 < 100001 and dist[nowNode*2] > nowDist:
        dist[nowNode*2]=nowDist
        heapq.heappush(pq,(nowDist,nowNode*2))







