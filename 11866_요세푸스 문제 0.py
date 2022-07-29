from collections import deque

queue = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)
#큐를 사용하여 푼다.
#k번째라면 answer 리스트에 추가하고 다음 숫자부터 인덱스가 초기화 되기 때문에 (원형) k앞에 숫자들을 뽑아서 뒤로 붙여나간다.
#queue가 빌때까지 반복한다.
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print('<', end="")
for i in range(len(answer)) :
    if i == len(answer)-1:
        print(answer[i], end="")
    else :
        print(answer[i] , end =", ")
print('>', end="")
