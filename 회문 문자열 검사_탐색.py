n = int(input())
for i in range(n):
    a = input()
    a = a.lower()
    if a == a[::-1]:
        print(f"#{i+1} YES")
    else :
        print(f"#{i+1} NO")

#[::-1]쓰지 않고 직접 구현#

n = int(input())
for i in range(n):
    a = input()
    a = a.lower()
    for j in range(len(a)//2):
        if a[j] != a[-1-j] :
            print(f"#{i+1} NO")
            break
    else :
        print(f"#{i + 1} YES")