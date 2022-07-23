#list comperehension#
# 0부터 19까지 수 중에서 홀수만 포함하는 리스트 만들기
a = [i for i in range(20) if i %2 ==1]
print(a)
#1부터 9까지 수 의 제곱값을 포함하는 리스트
a = [i*i for i in range(1,10)]
print(a)
#2차원 배열만들기
n=3
m=4
array = [[0]*m for _ in range(n)]
print(array)
#특정한 값의 원소를 모두제거 하는 법
a = [1,2,3,4,5,6,7,8,9]
remove_set = {3,4}
result = [i for i in a if i not in remove_set]
print(result)

##문자열자료형##
#"" 사용하기
print("don't you know \"Python\"?")

#dictionary
data = dict()
data["apple"]=1
data['banana']=2
data['kiwi']=3

if 'apple' in data:
    print("apple exits in the list \"data\"")

key_list=data.keys()
value_list = data.values()
print(value_list)

#반복문
#continue의 사용
#80점 이상이면 합격 하지만 블랙리스트인 2번학생과 4번학생은 제외

s = [90,85,77,65,97]
black_list = {2,4}

for idx, score in enumerate(s):
    if idx + 1 in black_list:
        continue
    if score> 80 :
        print("%d 번 학생은 %d점으로 합격입니다" %(idx+1, score))

#readline()사용 소스코드 예시

import sys
data= sys.stdin.readline().strip()
print(data)

#fstring 사용법
ans = 7
print(f"정답은 {ans}입니다")

#itertools 로 순열 조합구하기
#순열
from itertools import permutations
data = ["a",'b','c']
result = list(permutations(data,3)) #permutation은 클래스이기 때문에 list자료형으로 변환하여 사용한다.
print(result, len(result))

from itertools import product
result = list(product(data,repeat = 3)) #3개뽑는 모든 순열 구하기(중복허용)
print(result, len(result))

#조합
from itertools import combinations
data = ["a",'b','c']
result = list(combinations(data,3))
print(result,len(result))

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,3))
print(result,len(result))

import heapq

def heapsort(iterable):
    h =[]
    result = []
    #모든원소를 차례대로 힙에 삽입
    for value in iterable :
        heapq.heappush(h,value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

print(heapsort([1,3,5,7,9,2,4,6,8]))

#파이썬에선 maxheap을 제공하지 않는다. 따라서 최대힙을 구현하기 위해선 원소의 부호를 임시로 변경한다.
#힙에 원소를 삽입하기 전 부호를 반대로 바꾸었다가 힙에서 원소를 꺼낸 후 다시 원소의 부호를 바꾸면된다.

import heapq
def heapsort(iterable):
    h=[]
    result =[]
    for value in iterable :
        heapq.heappush(h, -value) #부호가 반대로 들어간다

    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) #부호를 다시 바꿔서 뺀

    return result

print(heapsort([1,3,5,7,9,2,4,6,8]))

heapsort([1,3,5,7,9,2,4,6,8,0])
