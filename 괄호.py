b = input()
cnt=0
s = []

for i in b:
    s.append(i)

for _ in range(len(b)):
    a = s.pop()
    if a == ")":
        cnt+=1
    elif a == '(':
        cnt-=1
    if cnt<0 :
        print("NO")
        break
if cnt ==0:
    print("YES")
elif cnt >0:
    print("NO")


