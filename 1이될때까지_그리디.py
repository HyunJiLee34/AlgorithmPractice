n,k = map(int,input().split())
cnt=0
# #나누는 것이 최소한의 횟수로 연산하게 한다
# #나누어지지 않으면 -1하기
while n!=1 :
    if n%k ==0 :
        n=n//k
        cnt+=1
    elif n%k!=0 :
        n-=1
        cnt += 1
print(cnt)


#해설코드#

while True :
    target =(n//k)*k #n이 k로 나누어 떨어지는 가장 가까운 수를 target에 저장
    cnt = cnt+(n-target) #target이 될때 까지 수행해야하는 -1연산의 횟수
    n=target
    #더이상 나눌수 없는 경우 반복문 탈출
    if n<k:
        break
    #n을 k로 나누기
    cnt+=1
    n=n//k

cnt = cnt+(n-1)# n은 아직 1이 아니기때문에 1이 될때까지의연산횟수 더해줘야한다
print(cnt)