import heapq
INF = 9876543210
N,M = map(int,input().split())

visited = [[-1 for i in range(N)] for j in range(M)]
visited[0][0]=1
dist=[[INF for i in range(N)]for j in range(M)]
dist[0][0]=0 #가중치
pq=[(0,0,0)] #가중치, 위치


L = []
for i in range(M):
    temp = list(map(int,input()))
    L.append(temp)

dR = [-1,1,0,0]
dC = [0,0,-1,1]

while(pq):
    nowDist,c,r = heapq.heappop(pq)
    if c == N-1 and r == M-1 :
        print(nowDist)
        break
    for i in range(4):
        nextR = r+dR[i]
        nextC = c + dC[i]
        if 0<=nextR<M and 0<=nextC<N and visited[nextR][nextC]==-1 :
            addedDist = nowDist + L[nextR][nextC]
            if dist[nextR][nextC]>addedDist :
                dist[nextR][nextC] = addedDist
                heapq.heappush(pq,[addedDist,nextC,nextR])
                visited[nextR][nextC]=1






