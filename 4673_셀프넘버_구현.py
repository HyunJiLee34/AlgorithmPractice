L = set()
for i in range(1,10001):
    for j in str(i):
        i = i + int(j)
        L.add(i)

numbers = set(range(1,10001))
print(numbers)
print(L)
self_num =sorted(numbers - L)

for i in self_num:
    print(i)





# # d(n)계산을 위한 함수 구현
# def D(x):
#     A = x
#     for i in str(x):
#         A += int(i)
#     return A

numbers = set(range(1,10001))
a = set()
for i in range(1, 10001):
    A= i
    for j in str(i):
        A += int(j)
    a.add(A)

res = sorted(numbers - a)

for i in res:
    print(i)






