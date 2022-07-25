def reverse(x):
    wordL = []
    for i in str(x):
        wordL.append(str(i))
    wordL.reverse()
    res = int("".join(wordL)) #int는 019 같은건 자동으로 0을 제외해서 만들어줌
    return res

def isPrime(x):
    if x ==1 :
        return False
    for i in range(2,x//2+1): #전체가 아니라 절반만 돌아도 소수 판별가능
        if x%i == 0 :
            return False
    else :
        return True


n = int(input())
a = list(map(int, input().split()))

for i in a :
    rev = reverse(i)
    if isPrime(rev):
        print(rev, end =" ")
