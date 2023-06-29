# file copy program  이거 명령 프롬포트에서 메모장 복사해서 만들어서 하거나 손수 일일이 만든 메모장 가지고 하는거임!

while True:
    file1=input('원본 파일 이름을 입력하세요')
    file2=input('복사 파일 이름을 입력하세요')

    infile=open(file1,'rb')
    outfile=open(file2,'wb')

    
    while True:
        cp_buffer=infile.read(1024)
        if not cp_buffer:
            break
        outfile.write(cp_buffer)
        

    infile.close()
    outfile.close()
    print(file1+ '을' +file2+'로 복사하였습니다.')
    
    print(infile.read(20))
    infile.close()
