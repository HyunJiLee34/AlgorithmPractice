
from collections import deque

n, k = map(int, input().split())
visited = [-1] * (100001)

q = deque()
q.append(n)
visited[n]=0

while q:
    nownode = q.popleft()
    if nownode == k:
        print(visited[nownode])
        break
    for nextnode in (nownode - 1, nownode + 1, 2 * nownode):
        if 0 <= nextnode < 100001 and visited[nextnode] == -1:  # 범위 내이고 방문하지 않았다면
            if nextnode == 2 * nownode:  # 순간이동
                visited[nextnode] = visited[nownode]
                q.appendleft(nextnode) #2*nownode가 다른 연산보다 더 높은 우선순위 가 #최단시간

            elif nextnode == nownode - 1 or nextnode == nownode + 1:
                visited[nextnode] = visited[nownode] + 1
                q.append(nextnode)




