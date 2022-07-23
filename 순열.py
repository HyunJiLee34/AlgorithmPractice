# template
n, r = map(int, input().split())
result = [0 for _ in range(5)]
check = [0 for _ in range(5)]


def getResult(x):
    # x번째 for문을 돌려야함.
    if x >= r:
        for i in result:
            if i != 0:
                print(i, end='')
        print()
    else:
        for i in range(n):
            if check[i] == False:
                print(check)
                alpha = ord('a') + i
                result[x] = chr(alpha)
                check[i] = True
                getResult(x + 1)
                print(check)
                check[i] = False

getResult(0)
