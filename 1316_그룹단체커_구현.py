N = int(input())

for i in range(N):
    temp = input()
    for j in range(0,len(temp)-1):
        if temp[j]==temp[j+1]:
            continue
        elif temp[j] in temp[j+1:]:
            N = N-1
            break
print(N)












