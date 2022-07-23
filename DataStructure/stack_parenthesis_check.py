class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return len(self.stack) == 0
    def pop(self):
        if len(self.stack)!=0:
            return self.stack.pop(-1)

def stackchecking(statement):
    stack = Stack()
    size = 0
    flag = "Wrong"
    for ch in statement:
        if ch in ("{","[","("):
            size +=1
            stack.push(ch)
        elif ch in ("}","]",")"):
            size +=1
            if stack.isEmpty():
                return (f'{flag}_{size}')
            else :
                left = stack.pop()
                if (left == '{' and ch !="}") or (left == '[' and ch !="]") or (left == '(' and ch !=")"):
                    return (f'{flag}_{size}')
    if stack.isEmpty():
        flag = "OK"
        return (f'{flag}_{size}')
    else :
        retu›rn (f'{flag}_{size}')


input_s = input("입력하시오 : ")
result = stackchecking(input_s)
print(result)
