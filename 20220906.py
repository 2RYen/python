import turtle as t
import random


def square(length):
    kind=random.choice([3,4,5,6])
#    kind=random.randint(3,6)
    for i in range(kind):
        t.fd(length)
        t.lt(360//kind)

def drawit(zx,zy):
    t.pu()
    t.goto(zx,zy)
    t.write('('+str(int(zx))+','+str(int(zy))+')')
    t.pd()
    t.begin_fill()
    t.color('green')
    square(25)
    t.end_fill()

t.onscreenclick(drawit)




# ASCII code -> American Standard Code for Information Interchange
