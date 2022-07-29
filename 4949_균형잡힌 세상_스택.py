#flag풀이#

stack = []
while True :
    a = input().rstrip()
    flag = True
    stack = []
    if a == '.': #.이 나오면 중단
        break
    for i in range(len(a)):
        if a[i]=='(' or a[i]=='[':
            stack.append(a[i])
        elif stack and (a[i]==')' or a[i]==']'): #열린괄호가 들어가 있고 닫는 괄호가 들어올때
            if a[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif a[i] == ']' and stack[-1] == '[':
                stack.pop()
            else : #짝이 맞지 않는 경우
                flag=False
                break # 더이상 다음 문자 보지 않고 다음 for문으로 이동
        elif not stack and (a[i]==')' or a[i]==']'): #닫힌 괄호가 바로 나올 때 바로 중단
            flag = False
            break
    if flag and not stack :
        print('yes')
    else :
        print('no')

#print - break 풀이#
stack = []
while True :
    a = input().rstrip()
    stack = []
    if a == '.':
        break
    for i in range(len(a)):
        if a[i]=='(' or a[i]=='[':
            stack.append(a[i])
        elif stack and (a[i]==')' or a[i]==']'):
            if a[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif a[i] == ']' and stack[-1] == '[':
                stack.pop()
            else :
                print("no")
                break
        elif not stack and (a[i]==')' or a[i]==']'): #바로 닫힌괄호가 오는 경우
            print("no")
            break
    else :
        if stack :
            print("no")
        else :
            print("yes")
