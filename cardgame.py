A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_win = 0
b_win = 0
for i in range(10):
    if A[i] > B[i] :
        a_win+=1
    elif A[i] < B[i] :
        b_win += 1

if a_win>b_win :
    print("A")
elif a_win<b_win :
    print("B")
else :
    print("D")