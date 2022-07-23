class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDequeue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.front = None
    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node= node.next
            count += 1
        return count

    def print(self):
        node = self.front
        print(" ", end=" ")
        while not node == None:
            print(node.data, end = " ")
            node = node.next
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
        elif self.isEmpty():
            print("underflow")


if __name__ == '__main__':
    N = int(input("연산의 개수 : "))
    q = DoublyLinkedDequeue()

    for i in range(N):
        inputs = input().split()
        operation = inputs[0]
        if operation == 'AF':
            pos = int(inputs[1])
            q.addFront(pos)
        elif operation == 'AR':
            pos = int(inputs[1])
            q.addRear(pos)
        elif operation == 'DF':
            q.deleteFront()
        elif operation == 'DR':
            q.deleteRear()
        elif operation == 'P':
            q.print()