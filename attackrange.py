N = int(input())
X,Y,R = map(int, input().split())

MAP = [[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i ==X-1 and j == Y-1 :
            MAP[X-1][Y-1]='x' #현재위치를 나타내기

for i in range(N):
    for j in range(N):
        for k in range(R): #k=0,1,2
            if abs(i-(X-1)) + abs(j-(Y-1)) == k+1 :
                MAP[i][j]=k+1
print(MAP)
