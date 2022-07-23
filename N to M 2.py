N,M = map(int,input().split())
cnt = 0
for i in range(N, M+1) :
    print(i, end=' ')
    cnt +=1
    if cnt == 8:
        print("")
        cnt =0

