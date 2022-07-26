n  = int(input())
tmp = list(map(int, input().split()))
score = 0
tmpscore = 0
for i in range(n) :
    if tmp[i] == 1:
        tmpscore += 1
        score += tmpscore
    elif tmp[i] == 0 :
        tmpscore = 0

print(score)