N,K= map(int, input().split())
L = []
for i in range(1, N+1):
    if N%i == 0 :
        L.append(i)

if len(L)< K :
    print(-1)
else :
    print(sorted(L)[K-1])

#2번째 방법
N,K = map(int, input().split())
cnt=0
for i in range(len(N)):
    if N%i ==0:
        cnt +=1 #약수 개수 카운트
    if cnt == K:
        print(i)
        break
else : #정상적으로 끝나면 else실행
    print(-1)
