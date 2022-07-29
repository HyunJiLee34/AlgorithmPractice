import sys
stack = []
n = int(sys.stdin.readline())

def size():
    return len(stack)

def push (x):
    stack.append(x)
    return stack

def pop():
    if size() == 0:
        return -1
    a = stack.pop()
    return a


def empty():
    if size()==0 :
        return 1
    else :
        return 0

def top():
    if size() == 0:
        return -1
    else :
        return stack[-1]

for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0]== 'push' :
        push(a[1])
    elif a[0] == 'top' :
        print(top())
    elif a[0] == 'size' :
        print(size())
    elif a[0] == 'pop':
        print(pop())
    elif a[0] == 'empty':
        print(empty())

#코드 길이 줄이기#
import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0]=="push" : 
        stack.append(a[1])
    if a[0] == 'pop':
        print(stack.pop() if len(stack) else -1)