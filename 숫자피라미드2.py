N,S = map(int, input().split())
L=[0 for _ in range(200)]
for i in range(1, N+1): # i = 1,2,3,4,5
    print(" "* int(N-i), end ="") # 4 3 2 1
    if i%2 ==1 : #홀수는 반대로 :
        for j in range(1,2*i): #한층에 몇개의 숫자를 넣을것인가
            L[j]= S
            S=S+1
            if S ==10 :
                S=1
            # print(L)
        for p in range(2*i-1,0,-1):
            print(L[p], end='')
    else : # 짝수는 그대로
        for k in range(1, 2 * i):
            print(S, end='')
            S=S+1
            if S==10 :
                s=1

    print()