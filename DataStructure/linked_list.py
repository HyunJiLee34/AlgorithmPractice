class DList :
    class Node: #노드생성
        def __init__(self,prev,item,next):
            self.prev = prev
            self.item = item
            self.next = next
    def __init__(self): #이중연결리스트생성
        self.head = self.Node(None,None,None) #꼬리 노드가 만들어지지않았기에 가리킬게없음
        self.tail = self.Node(self.head, None, None)
        self.head.next = self.tail #꼬리노드가 만들어져서 head의 next를 tail로로
        self.size = 0
    def size(self):
        return self.size #항목수
    def is_empty(self):
        return self.size == 0 #항목이 하나도 없다.
    def add(self, pos, item):
        p =self.head
        for i in range(pos):
            p=p.next
        t = p.prev
        n = self.Node(t, item, p)
        t.next = n
        p.prev = n
        self.size +=1
    def delete(self, pos):
        if self.size <pos :
            return "Invalid position"
        p = self.head
        for i in range(pos):
            p=p.next
        t = p.prev
        q = p.next
        t.next =q
        q.prev =t
        self.size -=1
    def get(self,pos):
        if self.size < pos :
            return "Invalid position"
        p = self.head
        for i in range(pos):
            p=p.next
        return p.item
    def print(self):
        if self.is_empty():
            print("List is empty.")
        else :
            p = self.head.next
            while p != self.tail:
                if p.next!= self.tail:
                    print(p.item, end="")
                else :
                    print(p.item)
                p = p.next

if __name__ == "__main__":
    num = int(input("Number of operations : "))
    List = DList()
    for i in range(num):
        inputs = input().split() # split()으로 처리
        operation = inputs[0]  # 리스트에 순서대로담아짐
        if operation == 'A':
            pos = int(inputs[1])
            alphabet = inputs[-1]
            List.add(pos, alphabet)
        elif operation == 'D':
            pos = int(inputs[1])
            List.delete(pos)
        elif operation == 'G':
            pos = int(inputs[1])
            print(List.get(pos))
        elif operation == 'P':
            List.print()



