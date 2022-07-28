types = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] #갈수있는 경우 정의
#이 문제는 좀 신기한 케이스이다 한칸 씩이 아니라 조건이 두칸씩간 뒤 한칸 이동 처럼 특정되어있기 때문에 하나씩 정의해주었다.
a = input()
row = int(a[1])
column = int(ord(a[0])) - int(ord('a')) + 1
# 열을 알파벳으로 받는다. 이를 숫자로 변경해주는 아이디어는 ord를 통해 숫자로 변경해준 다음 a의 숫자형을 빼주고 1을 더하는 것이다. (a가 1이니까)
rescnt = 0
for i in types:
    nr = row + i[0]
    nc = column + i[1]
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8: #격자판에서 나가지 않아야한다
        rescnt += 1

print(rescnt)