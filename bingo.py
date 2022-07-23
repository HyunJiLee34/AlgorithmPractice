def isbingo(arr):
    sum = 0
    for x in arr:
        if x.count(0) == 5:
            sum += 1
    for x in range(5):  # 세로
        zerocnt = 0
        for y in range(5):
            if board[y][x] == 0:
                zerocnt += 1
        if zerocnt == 5:
            sum += 1
    k = 0
    for x in range(5):
        if board[x][x] == 0:
            k += 1
    if k == 5:
        sum += 1

    a = 0
    for x in range(5):
        if board[x][4 - x] == 0:
            a += 1
    if a == 5:
        sum += 1
    return sum


board = []
mc=[]
for _ in range(5):
    temp = list(map(int,input().split()))
    board.append(temp)
for _ in range(5):
    temp = list(map(int, input().split()))
    for j in temp :
        mc.append(j)

for idx, num in enumerate(mc):
    for x in board :
        if num in x :
            x[x.index(num)] = 0
            break
    anscnt = isbingo(board)
    if anscnt >= 3 :
        print(idx+1)
        break


