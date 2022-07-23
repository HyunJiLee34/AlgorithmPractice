
# T = int(input())
#
# for i in range(T):
#     L = [1, 1, 2]
#     N = int(input())
#     for j in range(3,N+1):
#         L.append(L[j-3] +L[j-2] +L[j-1])
#     print(L[N])


X = int(input())
L = [0 for i in range(X+1)]

for j in range(X-1,0,-1):
    ansL = []

    a = j + 1
    b = 2*j
    c= 3*j
    if a <= X:
        ansL.append(L[a])
    if b <= X :
        ansL.append(L[b])
    if c <= X :
        ansL.append(L[c])
    L[j] = min(ansL)+1


print(L[1])

