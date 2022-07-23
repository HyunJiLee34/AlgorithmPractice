stack =[]
info = []
n, m = map(int, input().split())

for i in range(m):
    row = list(map(int, input().split()))
    info.append(row)

def push(data):
    global stack
    if len(stack)<n:
        stack.append(data)
    else :
        print("Overflow")

def top():
    global stack
    if len(stack)>0:
        print(stack[-1])
    else :
        print("NULL")

def pop():
    global stack
    if len(stack)==0:
        print("Underflow")
    else :
        del stack[-1]


for i in info:
    if i[0]==1 :
        push(i[1])
    elif i[0]==2 :
        pop()
    elif i[0]==3 :
        top()




