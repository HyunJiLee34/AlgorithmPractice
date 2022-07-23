import heapq
INF = 9876543210
t=1
while True :
    L = []
    N = int(input())
    if N==0:
        break
    for i in range(N):
        temp = list(map(int,input().split()))
        L.append(temp)
    visited = [[-1 for i in range (N)] for j in range(N)]
    pq = [(L[0][0],0,0)] #dist, R,C
    dist = [[INF for i in range(N)]for j in range(N)]
    dist[0][0]=L[0][0]
    dR = [-1,1,0,0]
    dC = [0,0,-1,1]
    while (pq):
        nowDist,R,C = heapq.heappop(pq)

        if dist[R][C] < nowDist:
            continue

        if R == N - 1 and C == N - 1:
            print(f"Problem {t}: {dist[N - 1][N - 1]}")
            break

        for i in range(4):
            nextR = R + dR[i]
            nextC = C + dC[i]
            if 0<=nextR<N and 0<=nextC<N :
                addedDist = dist[R][C]+ L[nextR][nextC]

                if addedDist < dist[nextR][nextC] :
                    dist[nextR][nextC]= addedDist
                    heapq.heappush(pq,((addedDist,nextR,nextC)))

    t+=1