n= int(input())
L = list(map(int,input().split()))
L.sort()
sumTime = 0
totalTime = 0
for i in range(n):
    sumTime +=L[i]
    totalTime+=sumTime

print(totalTime)