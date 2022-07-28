n = int(input())
a = input().split()

types = ["U", "D", "L", "R"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nowx, nowy = 1, 1

for i in a:
    for j in range(len(types)):
        if i == types[j]:
            nx = nowx + dx[j]
            ny = nowy + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    nowx, nowy = nx, ny

print(nowx, nowy)
