# 출력(숫자 출력 기능)
# 증가 기능(숫자 증가 기능)
# 초기화 기능(숫자를 0으로 만드는 기능)


'''class Counter:
    def output(self):
        return self.juho
    def step(self):
        self.juho=self.juho+1         # self.juho+=1
    def decrement(self):
        self.juho=self.juho-1
    def reset(self):
        self.juho=0'''

from turtle import *

t1=Turtle()  # 4각형
t1.shape('circle')

t2=Turtle()  # 5각형
t2.shape('square')

t3=Turtle()  # 6각
t3.shape('turtle')

t3.pu()
t3.color('red')
t3.goto(150,150)

t2.pu()
t2.color('blue')
t2.goto(-130,130)

t1.pu()
t1.color('green')
t1.goto(-110,-110)
t1.speed(0)

while True:
    t3.pd()
    for k in range(4):
        t3.fd(50)
        t3.left(90)
    t2.pd()
    for k in range(5):
        t2.fd(50)
        t2.left(360/5)
    t1.pd()
    for k in range(6):
        t1.fd(50)
        t1.left(360/6)










    
