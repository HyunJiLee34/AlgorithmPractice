N = int(input())

for i in range(N):
    temp = input()
    for j in range(0,len(temp)-1):
        if temp[j]==temp[j+1]:
            continue
        elif temp[j] in temp[j+1:]:
            N = N-1
            break
print(N)


#2022-07-26#


n= int(input())
cnt=0
for _ in range(n):
    W = input()
    L = []
    for i in range(len(W)):
        if W[i] not in L :
            L.append(W[i])
        elif W[i] in L and W[i-1]!= W[i]:
            n-=1
            break
print(n)











