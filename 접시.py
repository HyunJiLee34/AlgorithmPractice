from collections import deque

a=deque(["d","c","b","a"])
target = input()
ans = "impossible"
cnt = 0
def dfs(before,after,cleaner,command):
    global ans

    # 종료조건
    cnt=0
    for i,dish in enumerate(after) :
        if target[i]==dish:
            cnt+=1
        else:
            return

    if cnt==len(target):
        ans = command
        return

    # 식기 세척기에 넣기(before에 남아있으면)
    if before:
        dish = before.pop()
        dfs(before, after, cleaner+[dish], command+["push"])
        before.append(dish)

    # 식기세척기에서 빼기
    if cleaner:
        dish = cleaner.pop()
        dfs(before, after+[dish], cleaner, command+['pop'])
        cleaner.append(dish)

dfs(a,[],[],[])
print(ans)