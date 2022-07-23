N,K = map(int, input().split())
# y=[1]
# for i in range(2, N+1):
#     if N%i ==0 :
#         y.append(i)
#
# if len(y)<K :
#     print(0)
# else :
#     print(y[K-1])

N,K = map(int, input().split())
cnt = 0

def f():
    global cnt
    isTrue = False
    for i in range(1, N+1):
        ans  = N%i
        if ans ==0 :
            cnt+=1
            if cnt == K:
                isTrue = True
                return i
    if isTrue == False :
        return 0
print(f())

# cnt = 0
# isTrue =False
#
# for i in range(1, N+1):
#     if N%i ==0:
#         cnt+=1
#         if cnt == K:
#          isTrue = True
#          print(i)
# if isTrue ==False :
#     print(0)



