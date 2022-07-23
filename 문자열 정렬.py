N = int(input())
L = []
for i in range(N):
    w = input()
    L.append(w)
print(*sorted(L))