# ------------------------

# 피보나치 수5 (10870)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 전수랑 전전수를 더한 것.
# 0 1

# 첫번째 피보나치 수 ~ 20번째 피보나치 수
# 피보나치 배열은 0 1로 시작
# n=int(input())
# pivo = [0,1]
# for i in range(2,21):
#   pivo.append(pivo[i-1] + pivo[i-2])
# print(pivo[n])


# ---------------------------------------
# 제로
# a=int(input())
# don=[]
# for i in range(a):
#   num=int(input())
#   if num == 0:
#     if don:
#         # don에 있는 값을 하나 지워요
#         don = [2,3,4,2,3,4]
#         del don[-1] -
#         # don.remove(don[-1])
#     else:
#       continue
#   else:
#     don.append(num)
# print(sum(don))


# import sys
# input = sys.stdin.readline

# for i in range(10000000):
#   int(input()) #sys.stdin.readline())

# ------------------------------

# 선입선출 = 큐
# 후입선출 -> 스택

import collections
# a는 리스트랑 비슷한 자료 구조이다.
a=collections.deque([1,2])
b = [1,2]
del b[-1]
# 후입 선출 -> 스택
a.append(3)
# [1,2]
print(a.pop())
# == del a[-1]
# 훨씬 시간이 단축 됨. -> 리스트의 길이가 길수록


# 큐
# a.append()
# a.popleft()

# a.appendleft()