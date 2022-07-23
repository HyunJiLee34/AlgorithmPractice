MAP = []
ans=[]
king_r=0
king_c = 0
three_c,three_r,two_c,two_r = -1,-1,-1,-1
for i in range(8):
    temp = list(map(int, input().split()))
    MAP.append(temp)

for i in range(8):
    for j in range(8):
        if MAP[i][j] ==1 :
            king_r = i
            king_c = j #킹의 위치 저장
#행부터 탐색
for k in range(8):
    if MAP[king_r][k] ==2 :
        two_c = k
    if MAP[king_r][k]==3 : #3이 여러개인 경우 가장 오른쪽의 3이 three_c가 될것이다.
        three_c = k

if two_c!=-1 and three_c!=-1:
    if king_c < three_c < two_c or two_c<three_c<king_c:  # 안잡히는경우
        ans.append(0)
    else:
        ans.append(1)

if two_c!=-1 and three_c == -1:
  ans.append(1)
#열탐색
for k in range(8):
    if MAP[k][king_c]==2 :
        two_r = k
    if MAP[k][king_c]==3 : #3이 여러개인 경우 가장 오른쪽의 3이 three_c가 될것이다.
        three_r = k


if two_r!=-1 and three_r!=-1 :
    if king_r < three_r < two_r or two_r<three_r<king_r:  # 안잡히는경우
        ans.append(0)
    elif king_r != two_r :
        ans.append(0)
    else:
        ans.append(1)
if two_r!=-1 and three_r == -1:
  ans.append(1)

#킹의 열과 행에 룩이 없는경우
if king_r!= two_r and king_c!= two_c:
    ans.append(0)
for k in ans :
    if ans.count(1)>=1 :
        print(1)
        break
    else :
        print(0)
        break
