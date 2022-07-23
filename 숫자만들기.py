ans = [[]for _ in range(100005)]
N= int(input())
r = 1000007
ans[0]=0
ans[1]=1
ans[2]=2
ans[3]=4

for i in range(4, N+1):
    ans[i]= ((ans[i-2])+(ans[i-1])+(ans[i-3]))%r
print(ans[N])