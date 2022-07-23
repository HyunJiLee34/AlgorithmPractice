h,w = map(int,input().split())
MAP = list(map(int,input().split()))
ans = 0
for i in range(1, w-1):
    left = max(MAP[:i])
    right = max(MAP[i+1:])

    compare = min(left,right)
    if MAP[i]< compare:
        ans+=compare-MAP[i]
print(ans)