n,k = map(int,input().split())
#갈수 있는 모든 경우의 수에서 최단거리를 구하자
from collections import deque
inf = 100000
tmp = [0]*(inf+1)

q = deque()
q.append(n)

while q :
    nownode = q.popleft()
    if nownode == k :
        print(tmp[nownode])
        break
    for i in (nownode-1, nownode+1, nownode*2):
        if  0<=i<=inf and tmp[i]==0 : #먼저 i가 인덱스 안에 있는지 부터 확인해야 tmp[i]를 할때 인덱스에러가 나지 않는다.
            tmp[i] = tmp[nownode]+1
            q.append(i)

