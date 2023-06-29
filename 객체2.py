import turtle as t
from tkinter import *

def fkq():
    gon=int(ent1.get())
    for k in range(gon):
        t.fd(100)
        t.lt(360/gon)
        
labin=Tk()

labin.title('라빈의 창')
    
labin.geometry('600x600+10+10')
    
qu1=Label(labin,text='몇 각형을 그릴까요?')
qu1.grid(row=0,column=0)
ent1=Entry(labin)
ent1.grid(row=0,column=1)
but1=Button(labin,text='라빈',width=6,bg='black',fg='white',command=fkq)
but1.grid(row=1,column=0)

labin.mainloop()

