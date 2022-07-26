s = input()
res = int(s[0])
for i in range(1,len(s)):
    num =  int(s[i])
    if num <=1 or res ==1: #두 수 중 하나라도 0 또는 1 인 경우 더하기 수행
        res+=num
    else :
        res*=num

print(res)

