n =int(input())

flag = True
for i in range(n):
    stack = []
    line = input()
    for j in line :
        if j =="(" :
            stack.append(j)
        elif j ==")":
            if stack :
                stack.pop()
            else : #아무것도 없는데 닫는괄호가 나오면 멈추고 no
                print("NO")
                break

    else : #for-else문으로 for문에서 한번도 break난 적이 없다면 else실행
        if not stack : #스택이 비어있다면
            print("YES")
        else : #스택이 비어있지 않다면
                print("NO")
