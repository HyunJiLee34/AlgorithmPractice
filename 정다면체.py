from collections import Counter
n,m = map(int, input().split())
temp = []
for i in range(1,n+1):
    for j in range(1, m+1):
        temp.append(i+j)

counter = Counter(temp) #counter로 딕셔너리형태 만들기

arrMax = -2147000000

for idx, values in counter.items():
    if values > arrMax :
        arrMax = values
for idx, values in counter.items():
    if values == arrMax :
        print(idx, end = ' ')




