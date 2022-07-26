n= int(input())
L = list(map(int,input().split()))
L.sort()
#1,2,2,3,4
cnt=0 #그룹에 포함된 모험가 수
res = 0 #그룹 수
for i in L:
    cnt+=1
    if cnt >=i :
        res+=1
        cnt=0 #다음그룹으로 넘어감
print(res)
