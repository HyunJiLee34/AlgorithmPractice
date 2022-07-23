n = int(input())
a = list(map(int, input().split()))
m = round(sum(a)/n)
min = 2147000000
for k,i in enumerate(a) :
    arrMin = abs(i - m)
    if arrMin < min :
        min = arrMin
        score = i
        num = k+1
    elif arrMin == min :
        if i > score  :
            score = i
            num = k+1

#평균과 평균에 가장 가까운학생의 번호
print(m, num)