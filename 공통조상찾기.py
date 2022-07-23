a,b,c = map(int,input().split())
graph ={}
colorx = []
colory = []
for i in range(a):
    graph[i]=[]
for _ in range(a-1):
    N,M = map(int,input().split())
    graph[M].append(N)

def ancestor(x):
    colorx.append(x)
    if x==0:
        return
    else:
        for k,v in graph.items():
            if x == k:
                # colorx.append(*v)
                ancestor(*v)
def ancestory(y):
    colory.append(y)
    if y==0:
        return
    else :
        for k,v in graph.items():
            if y ==k:
                # colory.append(*v)
                ancestory(*v)
ancestor(b)
ancestory(c)
flag=True
for i in range(len(colorx)):
    for j in range(len(colory)):
        if flag==True and colorx[i]==colory[j]:
           print(colorx[i])
           flag=False
           break
