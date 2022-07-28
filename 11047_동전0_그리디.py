n,k = map(int,input().split())
numL=[]
for i in range(n):
    numL.append(int(input()))
numL.sort(reverse=True)

rescnt = 0

for i in numL :
    rescnt += k//i
    k=k%i
#k보다 큰수로 나눈다하더라도 나머지는 그대로 k이다

print(rescnt)

#두번째 풀이방법#
n,k = map(int,input().split())
numL=[]
for i in range(n):
    numL.append(int(input()))
numL.sort(reverse=True)

rescnt = 0

for i in numL:
    if i<=k :
        rescnt +=k//i
        k= k-((k//i)*i) #rescnt로 나누면 안된다. 누적되고있으니까
print(rescnt)