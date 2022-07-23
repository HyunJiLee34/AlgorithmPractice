n, m  = map(int, input().split())
ans =[]
def f(n,m):
    for i in range(n,m+1):
        if i == 1 :
            pass
        for j in range(2, i):
            if i%j ==0 :
                return False
    return True
print(f(1,10))


