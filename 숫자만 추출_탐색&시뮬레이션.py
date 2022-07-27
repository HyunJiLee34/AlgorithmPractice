a= input()
L=[]
numL = ['1','2','3','4','5','6','7','8','9','0']

def division_half(x):
    cnt=0
    #x의 절반 (x/2) 이상에선 n의 약수가 존재하지 않는다.
    for i in range(1,(x//2)+1):
        if x%i ==0:
            cnt+=1
    cnt+=1 # x포함
    return cnt

for i in a :
    if i in numL:
        L.append(i)
res = int("".join(L))

print(res)
print(division_half(res))

##isdecimal()사용##

res = 0
s = input()
for x in s :
    if x.isdecimal():
        res = res*10+int(x) #숫자를 하나씩 더 배열할때마다 10의자리 수 만큼 올라감

print(res)