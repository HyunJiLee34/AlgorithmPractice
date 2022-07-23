# T = int(input())
# for i in range(T):
#     n,s,e,k = map(int, input().split())
#     a = list(map(int,input().split()))
#     print(sorted(a[s-1:e])[k-1])
    #틀렸음 . 출력 형식에 맞지 않음
#2번쨰 방법
import sys
T = int(input())
for i in range(T):
    n,s,e,k = map(int, sys.stdin.readline().split())
    a= list(map(int, sys.stdin.readline().split()))
    print("#%d %d" %(i+1, sorted(a[s-1:e])[k-1]))