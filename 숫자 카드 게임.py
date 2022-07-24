n,m = map(int, input().split())

res = []
for i in range(n):
    MAP = list(map(int, input().split()))
    nowMin = min(MAP)
    res.append(nowMin)
print(max(res))

#두번째 풀이법 res=0 와 max사용

n,m = map(int, input().split())
res =0
for i in range(n):
    MAP = list(map(int, input().split()))
    nowMin = min(MAP)
    res = max(res, nowMin)

print(res)