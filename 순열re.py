n,r = map(int, input().split())
check = [False for _ in range(n)]
result = [0 for _ in range(n)]
def D(x):
    if x>=r :
        for i in result :
            if i != 0:
                print(i, end='')
        print()
    else :
        for i in range(n):
            if check[i] == False :
                result[x] = chr(ord('a')+i)
                check[i]=True
                D(x+1)
                check[i]=False

D(0)