C, R = map(int,input().split())
MAP = []
available = []
firstone = [0 for i in range(C)]
maxcnt=0
ansindex = []
for i in range(R):
    temp = list(map(int,input().split()))
    MAP.append(temp)
MAP.append([1 for _ in range(C)]) # 다 가능한 열을 위한 추가 행 생성

for c in range(C):
    cnt = 0
    for r in range(R+1):
        if MAP[r][c] ==1:
            break
        else :
            cnt+=1

        firstone[c] = cnt #1이들어갈수있는걸 나타내준다
for i in range(c):
    if firstone[i]>=4:
        available.append(i)

for i in available :
    cnt=0
    for j in range(firstone[i]-4, firstone[i]):
        MAP[j][i] =1
    for k in range(R):
        if sum(MAP[k])== C:
            cnt+=1
        if cnt>maxcnt :
            maxcnt=cnt
            ansindex = i
    for a in range(firstone[i] - 4, firstone[i]):
        MAP[a][i] = 0
if cnt ==0 or available == [] :
    print(0, 0)
else :
    print(ansindex+1, maxcnt)


