#그냥 직관적으로 풀기
#너무 오래걸린다
# cnt=0
# n = int(input())
#
# for i in range(2, n+1):
#     for j in range(2, i) :
#         if i%j ==0:
#             break
#     else :
#         cnt+=1
# print(cnt)

#에라토스테네스 체로 풀기
n = int(input())
temp = [0]*(n+1)
cnt=0
for i in range(2, n+1):
    if temp[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            temp[j]=1

print(cnt)







