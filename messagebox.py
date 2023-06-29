import tkinter.messagebox as msgbox
from tkinter import*

def info():
    msgbox.showinfo('알림','정상적으로 결제 되었습니다.')

def warn():
    msgbox.showwarning('경고','지정하신 좌석은 매진 되었습니다.')

def error():
    msgbox.showerror('오류','한도초과 오류')

def okcancel():
    msgbox.askokcancel('확인/취소창','해당 좌석은 반려동물 동반석 입니다. 예매하시겠습니까?')
    
def retrycancel():
    ret=msgbox.askretrycancel('재시도/취소','다시 시도하시겠습니까?')
    if ret==1:
        print('재시도 : ',ret)
    elif ret==0:
        print('취소 : ',ret)
    
    else:
        print('etc:',ret)

def yesno():
    ret=msgbox.askyesno('예/아니오','해당 좌석은 커플석입니다. 예매하시겠습니까?')
    print(ret)

def yesnocancel():
    ret=msgbox.askyesnocancel(title=None, message='예매내역이 저장되지 않았습니다.\n 저장 후 프로그램을 종료하겠습니까?')
    print(ret)

root=Tk()
root.title('스튜디오 D의 GUI')
root.geometry('640x480')


Button(root, text='알림',command=info).pack()
Button(root, text='경고',command=warn).pack()
Button(root, text='오류',command=error).pack()
Button(root, text='확인/취소',command=okcancel).pack()
Button(root, text='재시도/취소',command=retrycancel).pack()
Button(root, text='예, 아니오',command=yesno).pack()
Button(root, text='예, 아니오, 취소',command=yesnocancel).pack()

root.mainloop()
