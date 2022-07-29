from collections import deque

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    imp = deque(map(int, input().split()))
    idx= deque(list(range(n))) #index번호 담아줌
    cnt=0
    while imp:
        if imp[0]==max(imp):
            cnt+=1
            imp.popleft()
            if idx.popleft() == m : # 몇번 문서인지 어떻게 확인하나 ? 인덱스로 번호를 정해주자
                print(cnt)
        else :
            imp.append(imp.popleft())
            idx.append(idx.popleft())
