n = int(input())
result = [0 for _ in range(30)]
cnt = 0


def getResult(mySum, idx):
    # 현재까지 구한 합이 mySum이다.
    # 그리고 지금, idx번째 숫자를 결정할 차례. 즉 result[idx]
    if (mySum == n):
        for i in range(idx):
            if i <= idx - 2:
                print(result[i], end='+')
            else:
                print(result[i], end='')
        print()
        global cnt
        cnt += 1
    else:
        myNumber = 0
        if idx == 0:
            myNumber = n - 1
        else:
            myNumber = n - mySum

        for i in range(myNumber, 0, -1):
            result[idx] = i
            if (idx > 0 and result[idx - 1] < result[idx]): continue
            getResult(mySum + i, idx + 1)


getResult(0, 0)
print(str(cnt))
