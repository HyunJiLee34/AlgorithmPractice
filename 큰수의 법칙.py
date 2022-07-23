n,m,k = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
first = a[n-1]
second = a[n-2]
result = 0

while True :
    for _ in range(k):
        if m ==0 :
            break
        result +=first
        m = m-1

    if m ==0 :
        break
    result +=second
    m=m-1

print(result)