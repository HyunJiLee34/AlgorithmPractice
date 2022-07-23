class MaxHeap :
    def __init__(self):
        self.heap=[]
        self.heap.append(0)

    def size(self):
        return len(self.heap)-1
    def isEmpty(self):
        return self.size()==0
    def Parent(self, i):
        return self.heap[i//2]
    def Left(self,i):
        return self.heap[i*2]
    def Right(self,i):
        return self.heap[i*2 +1]
    def display(self, msg = 'heaptree:'):
        print(msg, self.heap[1:])
    def insert(self,n):
        self.heap.append(n)#말단에 넣기
        i = self.size() #삽입한것 레벨
        while (self.Parent(i)< n and i!=1) : #삽입한것이 부모보다 크고 레벨이 1이기 전까지
            print("1상황보고 : ", self.heap[i])
            self.heap[i] = self.Parent(i)
            print("2상황보고 : ",self.heap[i])
            i = i//2
        self.heap[i]=n #최종적으로 자리잡기
    def delete(self):
        parent =1 #인덱스
        child =2 #인덱스
        if not self.isEmpty(): # 삭제할 노드가 있다면
            hroot = self.heap[1] # 삭제할것은 최상단 노드(루트)
            last = self.heap[self.size()] #마지막 노드
            while (child <= self.size()): # (자식인덱스가 트리높이 보다 작을때까지 )
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child+=1 #오른쪽 자식노드가 더크면 child인덱스 1증가
                if last>= self.heap[child]:
                    break;
                print("바꾸기전", self.heap[parent],self.heap[child] )
                self.heap[parent] = self.heap[child] # down-heap(부모자식위치 바꿈)
                # self.display()
                print("바꾼후", self.heap[parent], self.heap[child])
                parent = child

                print("parent=child", self.heap[parent], self.heap[child])
                child *=2;
                # print("child *2", self.heap[parent], self.heap[child])
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
if __name__ == '__main__':
    heap = MaxHeap()
    data = [2,5,4,8,9,3,7,3]
    for elem in data :
        heap.insert(elem)
    heap.display()
    heap.delete()
