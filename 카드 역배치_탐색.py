L = list(range(21))

for i in range(10):
    a,b = map(int, input().split())
    for j in range((b-a+1//2)):
        L[a+j],L[b-j] = L[b-j],L[a+j]

for x in L[1:]:
    print(x, end=" ")