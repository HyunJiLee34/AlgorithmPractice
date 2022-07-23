MAP = []


for i in range(5):
    temp = list(map(int,input().split()))
    MAP.append(temp)
dR = [-1,1,0,0]
dC = [0,0,-1,1]
copyM = [[0 for i in range(10)] for j in range(10)]
for i in range(5):
    for j in range(5):
        copyM[i][j]=MAP[i][j]

for i in range(5):
    for j in range(5):
        ans = []
        cnt = 0
        nownode = MAP[i][j] #현재위치 표시
        for k in range(4) : #상하좌우 돌기
            nextR = i+dR[k]
            nextC = j+dC[k]
            if 0<=nextR<5 and 0<=nextC<5:
                cnt+=1
                nextnode = MAP[nextR][nextC]
                if nextnode>nownode :
                    ans.append(nextnode)
        if len(ans)==cnt:
            copyM[i][j]='*'

for i in range(5):
    for j in range(5):
        print(copyM[i][j], end=" ")
    print()
