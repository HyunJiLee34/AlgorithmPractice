n = int(input())
k= 2*n-1
for i in range(1,n+1):
  print(" "* (n-i) + "*"*k + " "* (n-i))