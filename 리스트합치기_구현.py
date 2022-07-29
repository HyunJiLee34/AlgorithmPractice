n=int(input())
L1 = list(map(int, input().split()))
m = int(input())
L2 = list(map(int, input().split()))
p1=p2=0 #포인터지정
ans =[]

while p1<n and p2<m:
    if L1[p1]<=L2[p2]:
        ans.append(L1[p1])
        p1+=1
    elif L2[p2]<=L1[p1]:
        ans.append(L2[p2])
        p2+=1

if p1>=n :
    ans+=L2[p2:]
elif p2>=m :
    ans+=L1[p1:]
print(ans)