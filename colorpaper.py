MAP = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())

for k in range(1, N+1):
    k_x, k_y, width, height = map(int, input().split())
    for y in range(k_y, k_y + height):
        MAP[y][k_x:(k_x + width)] = [k] * width

for k in range(1, N+1):
    result = 0
    for cnt in range(101):
        result += MAP[cnt].count(k)
    print(result)