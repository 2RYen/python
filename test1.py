# binding -> 파이썬의 이벤트 처리 메소드 -> interrupt 인터럽트 [컴퓨터에 예상하지 않은 일이 발생한 상태]

from tkinter import *
import turtle as t

def action_1(tae):
    mess='마우스_1번(왼쪽) 버튼 : '+'('+str(tae.x)+','+str(tae.y)+')'+'\n'
    txt2.insert(END, mess)

def action_2(sung):
    mess='마우스_2번(가운데) 버튼 : '+'('+str(sung.x)+','+str(sung.y)+')'+'\n'
    txt2.insert(END, mess)

def action_3(ju):
    mess='마우스_3번(오른쪽) 버튼 : '+'('+str(ju.x)+','+str(ju.y)+')'+'\n'
    txt2.insert(END, mess)

def whatKey(hyung):
    key=hyung.char
    mess='(타이핑 된 키보드는 '+key+'입니다.)'+'\n'
    txt2.insert(END, mess)
    if key=='a':
        t.back(10)
    elif key=='d':
        t.fd(10)
    elif key=='w':
        t.left(90)
        t.fd(10)
    elif key=='s':
        t.right(90)
        t.fd(10)
    else:
        txt2.insert(END,'키보드 입력 오류'+'\n')

def takein(minju):
    txt2.insert(END,'노란박스로 진입했어요'+'\n')
    for k in range(5):
        t.fd(100)
        t.left(144)
        
def takeout(minju):
    txt2.insert(END,'노란박스를 벗어났어요'+'\n')
    t.bye()

win=Tk()
win.geometry('300x600+100+100')
win.title("What's happen?")


txt1=Text(win,height=20, width=40, bg='yellow')
txt1.bind('<Button-1>', action_1)
txt1.bind('<Button-2>', action_2)
txt1.bind('<Button-3>', action_3)
txt1.bind('<Key>', whatKey)
txt1.bind('<Enter>', takein)
txt1.bind('<Leave>', takeout)
txt1.grid(row=0,column=0)

txt2=Text(win, height=20, width=40, bg='blue', fg='white')
txt2.grid(row=1,column=0)

t.

win.mainloop()
