N = int(input())
numbers =map(int, input().split())
ans = 0

for i in numbers :
    not_sosu=0
    if i > 1 :
        for j in range(2,i):
            if i %j == 0 :
                not_sosu+=1
        if not_sosu == 0:
            ans+=1
print(ans)

