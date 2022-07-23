N = int(input())
R = 1000007
ans = list()
ans[0]=0
ans[1]=1
ans[2]=2
for i in range(3, N+1):
    ans[i]= (ans[i-2]%R+ans[i-1]%R)%R
print(ans[N])
