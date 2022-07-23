class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [0] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def enqueue(self, item):
        if  self.isFull():
            print("overflow", *self.items[:])
        elif not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE  # 삽입 시 rear값을 하나 증가
            self.items[self.rear] = item  # 데이터를 큐에 삽

    def dequeue(self):
        if self.isEmpty():
            print("underflow")

        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE  # 삭제 시 front 값을 하나 증가
            self.items[self.front] = 0


if __name__ == '__main__':
    MAX_QSIZE = int(input("queue size : "))
    num = int(input("Number of operations : "))
    q = CircularQueue()

    for i in range(num):
        inputs = input().split()
        operation = inputs[0]
        if operation == 'I':
            pos = int(inputs[1])
            q.enqueue(pos)
        elif operation == 'D':
            q.dequeue()
        elif operation == 'P':
            print(*q.items[:])
