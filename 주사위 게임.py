n = int(input())
res = -21799999
for i in range(n):
    a,b,c = map(int, input().split())
    if a == b == c :
        nowsum = 10000+a*1000
    elif a==b and a!=c :
        nowsum = 1000+(a)*100
    elif a==c and b!=a :
        nowsum = 1000+(a)*100
    elif b==c and a!=b :
        nowsum = 1000 + (b) * 100
    elif a!=b!=c :
        nowsum = max(a,b,c)*100

    if nowsum > res :
        res = nowsum

print(res)

#다른 풀이#
#아예처음부터 정렬 시켜서 큰 숫자 찾기


n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int,tmp)
    if a == b and b == c :
        nowsum = 10000+a*1000
    elif a==b or a==c :
        nowsum = 1000+(a)*100
    elif b==c :
        nowsum = 1000 + (b) * 100
    else :
        nowsum =c * 100 #sort를 통해 자동 정렬됨됨