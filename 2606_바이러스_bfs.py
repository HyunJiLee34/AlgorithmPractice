from collections import deque
import sys
num_of_com = int(input())
conn_of_com = int(input())
graph = {}
for i in range(1, num_of_com+1):
    graph[i]=[]
for i in range(conn_of_com):
    N,M = map(int, sys.stdin.readline().rstrip().split())
    graph[N].append(M)
    graph[M].append(N)

q = deque([1])
cnt = 0
visited = [-1 for _ in range(num_of_com+1)]
visited[1]=1
while q :
    nowNode = q.popleft()
    for i in graph[nowNode]:
        if visited[i]== -1 :
            visited[i]=1
            cnt+=1
            q.append(i)
print(cnt)
