#틀린코드#
n = int(input())
km = list(map(int, input().split()))
pay = list(map(int, input().split()))
least = 999999999999
for i in range(len(pay) - 1):
    if pay[i] < least:
        least = pay[i]

p1 = 0
ans = 0
for i in range(n):
    if pay[p1] == least:
        ans = ans + (pay[p1] * (sum(km[p1:])))
        print(ans)
        break

    ans = ans + (km[p1] * pay[p1])
    p1 += 1

#정답코드#

n = int(input())
km = list(map(int, input().split()))
pay = list(map(int, input().split()))
least = pay[0]
ans = 0
for i in range(n-1):
    if pay[i]<least :
        least = pay[i]
    ans = ans + (least * km[i])

print(ans)