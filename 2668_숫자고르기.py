n = int(input())
L= [[] for _ in range(n+1)]

for i in range(n):
    L[i+1].append(int(input()))


# # 첫째줄에 뽑힌 수와 둘째줄에 뽑힌 수의 집합이 같아야함
# # 그런 경우의 수 중 가장 많은 원소를 고름
# # 사이클을 만드는 노드가 정답

ans = []
def dfs(top, k):
    visited[top] = True
    for w in L[top]:
        if not visited[w] :
            dfs(w,k)
        elif visited[w] and w==k :
            ans.append(w)#사이클형성





for k in range(1,n+1):
    visited = [False] * (n + 1)
    if not visited[k]:
        dfs(k, k)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])