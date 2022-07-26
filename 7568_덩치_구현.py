# N = int(input())
# L= []
# ans_L = []
#
# for i in range(N):
#     w,h = map(int, input().split())
#     L.append((w,h))
# for i in L :
#     rank =1
#     for j in L:
#         if i[0] < j[0] and i[1]< j[1] :
#             rank+=1
#     print(rank,end=' ')








n = int(input())
L = []
rank = [1]*n

for _ in range(n):
    w,h = map(int, input().split())
    L.append((w,h))

for i in range(n):
    for j in range(n): #(0,4)체크도 하고 (4,0)체크도해야함
        #왜냐하면 만약 4가 0보다 작은데 0,4만 체크하면 4의 랭크가 반영되지 않음

        if L[i][0]<L[j][0] and L[i][1]<L[j][1]:
            rank[i]+=1
print(*rank, end="")




