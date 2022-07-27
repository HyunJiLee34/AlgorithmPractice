num = int(input())


def hanoi(n, start, final, via):
    if n == 1:
        print(start, final)
        return
    else:
        hanoi(n - 1, start, via, final)
        print(start, final)
        hanoi(n - 1, via, final, start)


print(2 ** num - 1)
hanoi(num, 1, 3, 2)