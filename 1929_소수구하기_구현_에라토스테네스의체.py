from math import sqrt
M, N = map(int, input().split())
isPrime_list = [1 for _ in range(N+1)]
isPrime_list[0]=0
isPrime_list[1]=0

for num in range (2, N+1):
    if isPrime_list[num]==0 :
        continue
    for i in range(num*num,N+1,num) :
        isPrime_list[i]=0


for i in range(M,N+1):
    if isPrime_list[i] ==1 :
        print(i)