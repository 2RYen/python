from tkinter import*

def press(key):
    ent.insert(END,key)
    '''if key=='1':
        print('1이 눌러졌어요')
    elif key=='2':
        print('2가 눌러졌어요')
    else:
        print('나머지는 우리가')'''
        

def jongryo():  # calling
    ent.delete(0,END)
    ent.insert(END,'')  # '전화 거는중...'

pi_button=['도','레','미','파','솔','라','시','도','^']  # 1,2,3,4,5,6,7,8,9,#,0,*
win=Tk()
win.geometry('300x400+100+100')
win.title('피아노 건반')   # 모두의 창
ent=Entry(win,width=20,bg='gray')
ent.grid(row=0,column=0,columnspan=3) # 

r=1
c=0
for i in pi_button:
    cmd=lambda x=i : press(x)         # lambda 인수1, 인수2 : 수식
    but1=Button(win,text=i,width=6,height=6,bg='black',fg='white',font='고딕체 12', command=cmd)
    but1.grid(row=r,column=c)
    if c==2:
        r=r+1
        c=0
    else:
        c=c+1
but2=Button(win,text='종료',fg='red',bg='black',width=6,height=3,command=jongryo)
but2.grid(row=5,column=0,columnspan=3)

'''but2=Button(win,text='전화',fg='red',bg='black',width=6,height=3,command=caling)
but2.grid(row=5,column=0,columnspan=3)'''

win.mainloop()
