MAP = []
for i in range(9):
    temp = list(map(int, input().split()))
    MAP.append(temp)
def f():
    maxnum,maxarr,maxcol = 0,0,0
    for i in range(9):
        for j in range(9):
            if MAP[i][j]> maxnum :
                maxnum = MAP[i][j]
                maxarr,maxcol = i,j
            elif MAP[i][j] == maxnum :
                continue
    return maxnum, maxarr+1, maxcol+1

print(f()[0])
print(*f()[1:])
