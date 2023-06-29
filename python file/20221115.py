# --------알람시계(2884)---------
# a,b=map(int, input().split())

# if b>=45 and b<60:
#     print(a, b-45)
# elif 0<=b and b<45 :
#     if a>=1 :
#         print(a-1, b+15)
#     elif a<1 :
#         print('23', b+15)

# ----------------------------
# 더하기 사이클(1110)

# a=input()
# b=a
# count=0
# new=None
# while int(b) !=new:
#     if len(a) < 2:
#         a = "0"+a
#     new = a[-1]+str(int(a[0])+int(a[1]))[-1]
#     a = new
#     new = int(new)
#     count +=1
# print(count)

# -----------------------
# 설탕 배달(2839)

# sugar=int(input())  # 설탕 배달의 수 -> 3,5 / 배낭의 수가 최소가 되어야 함
# bag=0
# while sugar >= 0:
#     if sugar % 5 == 0:
#         bag += sugar//5
#         print(bag)
#         break
#     sugar-=3
#     bag += 1
# else:
#     print(-1)


# sugar=int(input())
# dp = [0,-1,-1,1,-1,1,2,-1,2,3,2,3]
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1~5000까지의 정답을 모두 가지고 있는 리스트
# print(dp[sugar])
# 6킬로가 남았을 때 최솟값 + 1(3킬로 짜리) = 9킬로의 최솟값

#  11
# 3  5 +1
# 8  6
# 2  2


# sugar=int(input())
# dp = [0,-1,-1,1,-1,1,2]

# if sugar >= 6:
#     # i = 7
#     for i in range(7,5001):
#         bag3 = dp[i-3] # -1
#         bag5 = dp[i-5] # -1
#         # 경우의 수 4가지 발동
#         # -1 -1 : 들고 가지 못함
#         if bag3 == -1 and bag5 == -1:
#             dp.append(-1)
#         elif bag3 != -1 and bag5 == -1:
#             dp.append(bag3+1)
#         elif bag3 == -1 and bag5 == -1:
#             dp.append(bag5+1)
#         elif bag3 != -1 and bag5 != -1:
#             dp.append(min(bag3,bag5)+1)
#     print(dp[sugar])
# else:
#     print(dp[sugar])
# print(dp[0:100])


        #/ 양수 -1 : 3킬로 가방은 가능 5킬로는 불가능 -> 3킬로를 담았을 때 최솟값 +1 / -1 양수 : 5킬로 가방은 가능 -> 5킬로 담았을 때 최솟값 +1 / 양수 양수