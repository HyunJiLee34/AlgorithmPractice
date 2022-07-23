N = int(input())
S=1
needplus = 1
plusrow = 2
for i in range(1,N+1):#줄이 몇번째줄인가
  for k in range(N-(i-1)): #한줄에입력되는 수
      if k == 0 :
          firstnum=S
      print(S, end=" ")
      S = S + needplus
      needplus+=1
  S = firstnum+plusrow
  plusrow+=1
  needplus=1 #초기화
  needplus=needplus+i
  print()


