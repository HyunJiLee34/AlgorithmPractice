A = input()
B = input()
flag=0
length=len(A)-len(B)
for i in range(0,length+1):
    cnt=0
    for j in range(0,len(B)):
        if A[i+j]==B[j]:
            cnt+=1
    if cnt== len(B):
        flag = 1
        print("YES")
if flag==0:
    print("NO")

