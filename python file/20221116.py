# ------
# 사분면 고르기

# x=int(input())
# y=int(input())

# if x>0 and y>0:
#   print(1)
# elif x>0 and y<0:
#   print(4)
# elif x<0 and y<0:
#   print(3)
# elif x<0 and y>0:
#   print(2)
# ------------------------
# 오븐시계

# h,m=map(int,input().split())
# t=int(input())
# if m+t>=60:
#   if h+((m+t)//60)>=24:
#     print(h+((m+t)//60)-24,(m+t)%60)
#   else:
#     print(h+(m+t)//60,(m+t)%60)
# else:
#   print(h,m+t)

# --------------------------------------------
# 주사위 세개

# a,b,c=map(int,input().split())
# if a== b ==c:
#   print(10000+a*1000)
# elif a==b or a==c:
#   print(1000 + a*100)
# elif b==c:
#   print(1000 + b*100)
# elif a != b != c:
#   if a>b and a>c:
#     print(a*100)
#   if b>a and b>c:
#     print(b*100)
#   if c>a and c>b:
#     print(c*100)

# ----------------------------
# 구구단

n=int(input())
i=1
while i<10:
  print(n,'*',i,'=',n*i)
  i=i+1

# ------------------------
# A + B -3

# t=int(input())

# for i in range(t):
#   a,b=map(int,input().split())
#   print(a+b)