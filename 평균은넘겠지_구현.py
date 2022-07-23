C = int(input())
for i in range(C) :
    temp = list(map(int, input().split()))
    avg = sum(temp[1:])/temp[0]
    cnt=0
    for score in temp[1:]:
        if score > avg :
            cnt+=1
    print(str('%.3f'% round(cnt/temp[0]*100,3))+'%')












