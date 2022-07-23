N = int(input())
score = list(map(int,input().split()))

M = max(score)
ans_L = []
for i in score :
    new_score = i/M*100
    ans_L.append(new_score)
print(round(sum(ans_L)/N,2))











