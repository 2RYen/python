# 10개씩 끊어 출력하기(11721)
# a=input()
# for i in range(0, len(a), 10):
#   print(a[i:i+10])

# -쌤이랑 같이 함-
# strs = input()
# prinStr = ""
# for char in strs:
#   prinStr += char
#   if len(prinStr) == 10:
#     print(prinStr)
#     prinStr=""
# print(prinStr)

# --------------------------------------
# 웇놀이(2490)  - 이상함. 수정해야 됨

# 도 개 걸 윷 모
# A  B  C  D  E
# 0 -> 배(뒤집)
# 1 -> 등(안뒤집)

# for i in range(3):
#   a = sum(list(map(int, input().split)))
#   if a == 3:
#     print("A")
#   elif a == 2:
#     print("B")
#   elif a == 1:
#     print("C")
#   elif a == 0:
#     print("D")
#   elif a == 4:
#     print("E")

# -------------------------------------------------------
# 알파벳 개수(10808)

# word = input()
# result = []
# als = "abcdefghijklmnopqrstuvwxyz"
# for al in als :
#   result.append(str(word.count(al)))
# for i in result:
#   print(i, end=" ")
# print(*result)
# print("+".join(result))

# --------------------
# 단어 길이 재기(2743)
# a= input()
# print(len(a))