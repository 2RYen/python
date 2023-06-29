# lambda = 즉흥적으로 쓰는 함수, 몸체가 없음, 무명의

# juho=[lambda x: x**2, lambda x:x**3, lambda x:x**4]
'''for k in juho:
	print(k(3))'''

'''hee=(lambda x,y: x if x<y else y)
    hee(4,5)'''

# hee(32,23546)


from tkinter import*
import winsound
import time

def check_do():
    winsound.Beep(261,1000//2)
def check_re():
    winsound.Beep(293,1000//2)
def check_mi():
    winsound.Beep(329,1000//2)
def check_fa():
    winsound.Beep(349,1000//2)
def check_sol():
    winsound.Beep(391,1000//2)
def check_ra():
    winsound.Beep(440,1000//2)
def check_si():
    winsound.Beep(493,1000//2)
def check_ddo():
    winsound.Beep(545,1000//2)



gitaek=Tk()
gitaek.geometry('650x200+100+100')
gitaek.title("민주의 Piano")
do=Button(gitaek,text='도',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_do)
do.grid(row=0,column=0)
re=Button(gitaek,text='레',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_re)
re.grid(row=0,column=1)
mi=Button(gitaek,text='미',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_mi)
mi.grid(row=0,column=2)
pa=Button(gitaek,text='파',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_fa)
pa.grid(row=0,column=3)
sol=Button(gitaek,text='솔',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_sol)
sol.grid(row=0,column=4)
ra=Button(gitaek,text='라',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_ra)
ra.grid(row=0,column=5)
si=Button(gitaek,text='시',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_si)
si.grid(row=0,column=6)
ddo=Button(gitaek,text='도',bg='black',fg='white',width=4,height=4,font='고딕체 20',command=check_ddo)
ddo.grid(row=0,column=7)
