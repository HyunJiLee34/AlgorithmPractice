import sys
from math import sqrt
M,N = map(int,input().split())

for num in range(M,N+1):
    if num%2 == 0 or num==1:
        continue
    not_sosu = 0
    for i in range(2,int(sqrt(num))+2):
        if num%i == 0 :
            not_sosu+=1
    if not_sosu == 0 :
        print(num)

import sys
from math import sqrt

M, N = map(int, input().split())

for num in range(M, N + 1):
    if num == 2 :
        print(num)
        continue #다음반복으로
    if num % 2 == 0 or num == 1:
        continue
    is_sosu = True
    for i in range(2, int(sqrt(num)) + 2):
        if num % i == 0:
            is_sosu = False
            break
    if is_sosu == True:
        print(num)



