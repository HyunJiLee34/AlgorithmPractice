n = int(input())
a = list(map(int, input().split()))

D = dict()


for keys in a:
    D[keys] = 0
    temp = 0
    for j in str(keys):
        temp+=int(j)
    D[keys] = temp

tempMax = -124700000
for idx, values in D.items():
    if values > tempMax :
        tempMax = values
        res = idx #가장먼저나온거 출력이니까 이렇게 해도됨
print(res)

#함수를 이용한 풀이
#자릿수의 합을 구해주는 함수


n = int(input())
a = list(map(int, input().split()))

D = dict()

for keys in a:
    D[keys] = 0

def digit_sum(x):
    temp = 0
    for j in str(x):
        temp+=int(j)
    return temp

for i in a :
    D[i] = digit_sum(i)

tempMax = -124700000
for idx, values in D.items():
    if values > tempMax :
        tempMax = values
        res = idx #가장먼저나온거 출력이니까 이렇게 해도됨
print(res)