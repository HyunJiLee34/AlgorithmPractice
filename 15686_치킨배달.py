from itertools import combinations
N,M = map(int,input().split())
L=[]
ckL = []
house= []
for i in range(N):
    temp = list(map(int,input().split()))
    L.append(temp)
for i in range(N):
    for j in range(N):
        if L[i][j] ==2 : #치킨집위치
            ckL.append((i,j))
        elif L[i][j]==1 : #집의 위치
            house.append((i,j))
answer=9999
for i in combinations(ckL,M) :
    # print(i)
    tmp = 0
    for h in house :
        # print("집시작1!!!!!!!!!!!!!!!!!!!!!!1")
        dist = 9999
        for k in i :
            # print(h, "집위치")
            # print(k,"치킨집위치")
            distance=abs(k[0] - h[0]) + abs(k[1] - h[1])
            # print(distance,"거리차이")
            dist = min(dist,distance)
            # print(dist,"최소거리")
        tmp += dist
        # print(tmp, "치킨거리합")
    answer = min(answer,tmp)
print(answer)
# comb = list(combinations(ckL,M))#남겨야하는 치킨집뽑음
# result = []
# for h in house :
#
#     distance = []
#     for i in range(len(comb)):
#         city_chicken_dist = 0
#         for k in comb[i]: #치킨집 조합
#             print(h,"집위치")
#             print(k,"치킨집위치")
#             distance.append(abs(h[0] - k[0]) + abs(h[1] - k[1]))
#         print(distance)
#         print(min(distance))
#     city_chicken_dist+=min(distance)
# print(city_chicken_dist)