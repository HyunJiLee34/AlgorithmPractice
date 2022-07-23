N, S = map(int, input().split())
L = [0 for _ in range(200)]
for i in range(1, N + 1):
    space = N - i
    print(" " * space, end="")
    if i % 2 == 1:
        for k in range(1, 2 * i):
            L[k] = S
            S = S + 1
            if S == 10:
                S = 1
        for p in range(2 * i - 1, 0, -1):
            print(L[p], end="")

    else:
        for j in range(1, 2 * i):
            print(S, end="")
            S = S + 1
            if S == 10:
                S = 1
    print()
