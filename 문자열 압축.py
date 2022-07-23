## template
L = input()
cnt = 1
ans =''
for i in range(1,len(L)):
    if L[i]==L[i-1]:
        cnt+=1
    else :
        if cnt!=1:
            ans= ans + str(cnt)+L[i-1]
            cnt=1
        else :
            ans+=''+ L[i-1]
if L[-1]==L[-2]:
    ans = ans + str(cnt)+L[-1]
else :
    ans = ans+''+L[-1]
print(ans)






