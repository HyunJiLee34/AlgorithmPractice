bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):
    if bracket[i]=='(':
        stack.append(bracket[i])
        tmp*2
    elif bracket[i]=='[':
        stack.append(bracket[i])
        tmp*3
    elif bracket[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        elif bracket[i-1]=="(":
