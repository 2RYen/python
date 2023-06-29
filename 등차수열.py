from tkinter import *

def save():
    inf=open(ent4.get(),'w')
    inf.write(txt1.get('0.0',END))    # 0.0=행과 열을 나타냄!
    inf.close()
         
def calc():
    ret=int(ent1.get())+(int(ent3.get())-1)*int(ent2.get())
    start=int(ent1.get())
    step=int(ent2.get())
    for num in range(start, ret+1, step):
        if num==ret:
            txt1.insert(END,str(num))
        else:
            txt1.insert(END,str(num)+',')           # num자리에 원래 ret가 들어갔음, 문자(string)는 +가 가능!
# print(num,end=' ')
# ret=int(ent1.get())+(int(ent3.get())-1)*int(ent2.get())
def clear():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    txt1.delete('0.0',END)
    ent4.delete(0,END)
def end():
    win.destroy()


win=Tk()
win.geometry('400x600+100+100')
win.title('등차수열 계산기')

fram1=Frame(win)
fram1.grid(row=1,column=0)
fram2=Frame(win)
fram2.grid(row=2,column=0)
fram3=Frame(win)
fram3.grid(row=3,column=0)
fram4=Frame(win)
fram4.grid(row=4,column=0)

lab0=Label(win,text='등차수열 계산기',fg='white',bg='black',font='고딕체 12')
lab0.grid(row=0,column=0)
lab1=Label(fram1,text='초 항',font='고딕체 11')
lab1.grid(row=0,column=0)
lab2=Label(fram1,text='공 차',font='고딕체 11')
lab2.grid(row=1,column=0)
lab3=Label(fram1,text='출력항',font='고딕체 11')
lab3.grid(row=2,column=0)

ent1=Entry(fram1,font='고딕체 11')
ent1.grid(row=0,column=1)
ent2=Entry(fram1,font='고딕체 11')
ent2.grid(row=1,column=1)
ent3=Entry(fram1,font='고딕체 11')
ent3.grid(row=2,column=1)

lab4=Label(fram2,text='결 과',font='고딕체 11')
lab4.grid(row=0,column=0)
txt1=Text(fram2,height=5,width=30,font='고딕체 11')
txt1.grid(row=1,column=1)

but1=Button(fram3,text='Calc',width=6,bg='black',fg='red',command=calc)
but1.grid(row=0,column=0)
but2=Button(fram3,text='Clear',width=6,bg='black',fg='red',command=clear)
but2.grid(row=0,column=1)
but3=Button(fram3,text='Save',width=6,bg='black',fg='red',command=save)
but3.grid(row=0,column=2)
but4=Button(fram3,text='Quit',width=6,bg='black',fg='red',command=end)
but4.grid(row=0,column=3)

lab5=Label(fram4,text='저장 위치',font='고딕체 11')
lab5.grid(row=0,column=0)
ent4=Entry(fram4,width=30,font='고딕체 11')
ent4.grid(row=0,column=1)

win.mainloop()
