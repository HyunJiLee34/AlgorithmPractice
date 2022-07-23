N = int(input())
V = list(range(1,N+1))
ans =0
for i in V:
    if i %2 == 0:
        ans+=i
print(ans)
