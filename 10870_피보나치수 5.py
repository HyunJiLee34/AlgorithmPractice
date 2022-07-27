def fibo(i):
    if i == 1:
        return 1
    elif i == 0:
        return 0
    return fibo(i - 2) + fibo(i - 1)


n = int(input())
print(fibo(n))