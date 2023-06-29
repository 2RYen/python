# 문제1

def solution(shirt_size):
    std_size=['XS','S','M','L','XL','XXL']
    howmany=[0,0,0,0,0,0]
    for user in shirt_size:
        howmany[std_size.index(user)]=howmany[std_size.index(user)]+1
    return howmany

user_size=['XS','S','L','L','XL','S']
x = solution(user_size)
print(x)


# 문제2

'''def solution2(grade):
    std_grade=['S','G','V']
    howmany=[0,0]
    for user in grade:
        howmany[std_grade.index(user)]=howmany[std_grade.index(user)]+1
    return howmany

user_grade=['V','S']
x=solution2(user_grade)
print(x)

def solution0(price):
    std_price=['5%','10%','15%']
    howmany=[0,0,0]
    for user in price:
        howmany[std_price.index(user)]=howmany=[std_price.index(user)]-100
    return howmany

user_price=['2500','96900']
x=solution2(user_price)
print(x)'''

# 문제3

def solution3(start_month):
    std_month=['31','28','31','30','31','30','31','31','30','31','30','31']
    howmany=[0,0,0,0,0]
    for year in start_month:
        howmany[std_month.index(year)]=howmany[std_month.index(year)]<=end_month
    return howmany

year_month=['1','2','2','2','31']
x=solution3(year_month)
print(x)

# 문제4

def solution4(arr):












