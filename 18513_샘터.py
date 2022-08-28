from collections import deque
from sys import stdin
input = stdin.readline

n, k =map(int, input().split()) #n개의 샘터 존재, k채의 집을 지을것
pond =list(map(int, input().split())) #샘터의 위치

#불행도의 합이 최소가 되어야한다
#bfs -1 +1이동
#pond에 가장 가깝게 집 배치?

q = deque()
visited = set() #일차원 배열 방문체크
dis_cnt = 0 #불행도 체크
house_cnt = 0 #지어진 집의 수

for i in pond :
    q.append((i, 0))
    visited.add(i)

while q :
    node, dis = q.popleft()
    for d in [-1,1]:
        nextnode = node + d
        if nextnode in visited :
            continue
        else :  #방문하지 않았다면
            visited.add(nextnode)
            dis_cnt+=dis+1 #최종 불행도 더하기
            house_cnt +=1
            q.append((nextnode, dis+1))
        if house_cnt == k:  # 메모리초과
            q = list()
            break

print(dis_cnt)




