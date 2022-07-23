M = int(input())
N = int(input())
isPrimeList = [1 for _ in range(N+1)]
isPrimeList[0]=0
isPrimeList[1]=0

for num in range(2, N+1):
    if isPrimeList[num]== 0:
        continue
    for i in range(num*num,N+1,num):
        isPrimeList[i]=0

sum_ans = 0
min_ans = 0
isPrime = False

for i in range(M,N+1):
    if isPrimeList[i]==1 :
        if isPrime == False :
            min_ans = i
            isPrime = True
        sum_ans+=i


if isPrime == False :
    print(-1)
else :
    print(sum_ans)
    print(min_ans)