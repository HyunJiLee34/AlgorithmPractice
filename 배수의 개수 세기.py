A,B,C =map(int, input().split())
ans=0
if A>B :
    A,B = B,A

for i in range(A, B + 1):
    if i %C == 0:
        ans +=1

print(ans)

