N = int(input())
ans_L = []
if N<=99 :
    ans_L = [i for i in range(1,N+1)]
    print(len(ans_L))
elif 99<N<=1000 :
    for i in range(1,100):
        ans_L=[i for i in range(1,100)]
    for i in range(100,N+1):
        a=str(i)
        if int(a[1]) - int(a[0]) ==int(a[2]) - int(a[1]) :
            ans_L.append(int(a))
    print(len(ans_L))










