a = input()
ans = []
num = 0
for i in a:
    if not i.isdecimal():
        ans.append(i)
    else:
        num += int(i)
ans.sort()

if num != 0:
    ans.append(str(num))

print(''.join(ans))
