from collections import deque
N = int(input())
q = deque([(1,0)])
L =[(0,0)]
ans = 0

def bfs():
    global ans
    while q :
        now_day, now_income = q.popleft()
        if now_day > N :
            if now_income > ans :
                ans = now_income
            continue
        add_day = L[now_day][0]
        add_income = L[now_day][1]
        # 상담하는경우
        if now_day+add_day <= N+1 : # 퇴사전
            day = now_day+add_day
            income = now_income+add_income
            q.append((day, income))
        # 하지않는경우
        q.append((now_day+1, now_income))

for i in range(N):
    a, b = map(int, input().split())
    L.append((a,b))

bfs()
print(ans)