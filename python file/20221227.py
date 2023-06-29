# 박사 과정(5026)
# n=int(input())
# for i in range(n):
#   question = input() # 2+2 or P=NP
#   if "+" in question:
#     a,b = question.split("+")
#     print(int(a)+int(b))
#   else:
#     print("skipped")  # +기호만 옴, 근데 +, -, * 세개가 다 올 수 있다면?


# 계산기 프로그램(5613) - 런타임 에러남
# 언제 끝날지 모름
# result = 0
# count = 0
# operator = ""
# # 0=숫자 1=연산자 2=숫자 3=연산자
# while True:
#   a = input() # 100, +, -, *, /
#   if a == "=":
#     print(result)
#     break
#   if count == 0:
#     result = int(a)
#     count += 1
#     continue
#   if count %2 ==1:
#     operator = a
#   else:
#     if operator == "+":
#       result += int(a)
#     elif operator == "-":
#       result -= int(a)
#     elif operator == "*":
#       result *= int(a)
#     elif operator == "/":
#       result //= int(a)
#   count +=1


# 네 수(10824)
# 10 20 30 40
# a,b,c,d = input().split(" ") #str
# a = a+b # 1020
# c = c+d # 3040
# print(int(a)+int(c)) # 4060
# print(int(a+b)+int(c+d))