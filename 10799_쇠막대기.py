bar = list(input())
answer = 0
L = []

for i in range(len(bar)):
    if bar[i] == '(':
        L.append('(')

    else:
        if bar[i-1] == '(':
            L.pop()
            answer += len(L)

        else:
            L.pop()
            answer += 1

print(answer)