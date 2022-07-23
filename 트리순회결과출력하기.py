node = int(input())
tree = [[] for _ in range(node)]
for i in range(node):
    a,b,c = list(map(int,input().split()))
    tree[a].append(b)
    tree[a].append(c)
def preorder(x):
    if tree[x][0]==-1 and tree[x][1]==-1:
        print(x,end=" ")
    else :
        print(x, end=" ")
        if tree[x][0]!=-1 :
            preorder(tree[x][0])
        if tree[x][1]!=-1:
            preorder(tree[x][1])
def inorder(x):#중위
    if tree[x][0]==-1 and tree[x][1]==-1:
        print(x,end=" ")
    else:
        if tree[x][0]!=-1:
            inorder(tree[x][0])
        print(x, end=" ")
        if tree[x][1]!=-1:
            inorder(tree[x][1])

def postorder(x):#후위순회
    if tree[x][0]==-1 and tree[x][1]==-1:
        print(x,end=" ")
    else :
        if tree[x][0]!=-1:
            postorder(tree[x][0])
        if tree[x][1]!=-1:
            postorder(tree[x][1])
        print(x, end=" ")
preorder(0)
print()
inorder(0)
print()
postorder(0)