# -가 나오는 순간부턴 다 빼주면 됨
n = input()
a = n.split('-')
ans = 0
for i in a[0].split('+'):  # 첫숫자는 더해준다.
    ans += int(i)
for i in a[1:]:
    for j in i.split("+"):
        ans -= int(j)

print(ans)