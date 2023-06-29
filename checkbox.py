from tkinter import*

def dap_check():
    if value1.get()==1 and value2.get()==0 and value3.get()==0 and value4.get()==1:
        print('정답')
    else:
        print('틀렸습니다')
    


win=Tk()

lab1=Label(win,text='[문제 1] 다음 중 프로그래밍 언어를 모두 고르시오',font='나눔고딕 16')
lab1.grid(row=0,column=0)

value1=IntVar()
a=Checkbutton(win,text='1. Python',variable=value1)
a.grid(row=1,column=0)            # row=행, column=열 / grid=창

value2=IntVar()
b=Checkbutton(win,text='2. Spring',variable=value2)
b.grid(row=2,column=0)

value3=IntVar()
c=Checkbutton(win,text='3. English',variable=value3)
c.grid(row=3,column=0)

value4=IntVar()
d=Checkbutton(win,text='4. Java script',variable=value4)
d.grid(row=4,column=0)

but1=Button(win,text='제출',fg='white',bg='black',width=6,command=dap_check)
but1.grid(row=5,column=0)

win.mainloop()
