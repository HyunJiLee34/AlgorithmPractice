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













