# 등차수열 계산기
# 초항 : 2 / 공차 : 3 / 출력항 : 7  // 결과 : 2 5 8 11 14 17 20


# 파일 탐색기 만들기

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readfile=askopenfilename()
if readfile != None:
    infile=open(readfile,'r')
    
for line in infile.readlines():
    line=line.strip()   # strip = enter 키 까지.
    print(line)

infile.close
