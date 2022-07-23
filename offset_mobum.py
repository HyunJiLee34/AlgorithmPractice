frame = []
outline = [[10 for _ in range(5)] for _ in range(5)]
for i in range(5):
    temp = list(map(int,input().split()))
    frame.append(temp)

for i in range(len(frame)):
    for j in range(len(frame[i])):
        outline[i + 1][j + 1] = 10
print(outline)