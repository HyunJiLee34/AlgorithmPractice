n,k = map(int, input().split())
a = list(map(int, input().split()))
L=set()
#3번 뽑는법 (for문 반복)
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            L.add(a[i]+a[j]+a[m])
#set은 sort가 없음 다시 list화해야함
L = list(L)
L.sort(reverse=True)
print(L[k-1])