N = int(input())
L = []
ans = [0 for _ in range(N)]

for i in range(N):
    temp=list(map(int, input().split()))
    L.append(temp)

for i in range(N): #i번 학생
    visited = [False for _ in range(N)]
    for grade in range(5): #학년
        for name in range(N):
            if name!=i and L[name][grade] == L[i][grade]:
                visited[name] = True

    ans[i] = len(list(filter(lambda x: x, visited)))

print(ans.index(max(ans))+1)







