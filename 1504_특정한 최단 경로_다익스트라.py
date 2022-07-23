import heapq
import sys

N,E = map(int, input().split())

graph = {}
INF =9876543210

for i in range(1,N+1):
    graph[i]=[]
for i in range(E):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int,input().split())
if E==0:
    print(-1)
    sys.exit(1)

def isVisited(L,dist):
    for node in L:
        if dist[node]==INF:
            return False
    return True

def route(startNode, L):
    dist = [INF for i in range(N + 1)]
    dist[startNode]=0
    pq = [(0,startNode)]
    size=len(L)
    visited=[0 for i in range(size)]

    while (pq):
        nowDist,nowNode = heapq.heappop(pq)


        if nowDist > dist[nowNode]:
            continue
        # print(nowNode,nowDist)
        if nowNode in L:
            visited[nowNode]=1
            if all(visited):
                ans=[]
                for node in L:
                    ans.append(dist[node])
                return ans

        for toNode, toDist in graph[nowNode]:
            addedDist = toDist + dist[nowNode]
            if addedDist < dist[toNode]:
                dist[toNode]= addedDist
                heapq.heappush(pq,(addedDist,toNode))


s1,s2=route(1,[v1,v2])
print("여기")
d1,d2=route(N,[v1,v2])
print("--")
A=route(v1,[v2])[0]

print(s1,s2,d1,d2,A)

if s1+d2<s2+d1:
    if s1+d2+A <= INF:
        print(s1+d2+A)
    else :
        print(-1)

else:
    if s2+d1+A <= INF :
        print(s2+d1+A)
    else :
        print(-1)



