import time

sm=open('C:\\Users\\mj031\\Desktop\\encript.txt','r')
cnt=0

for line in sm:
    #cnt+=1
    line=line.rstrip()
    for idx in range(len(line)-2):
        if line[idx]=='3' and line[idx+1]=='6' and line[idx+2]=='9':
            print(line)
#print('3의 갯수=',cnt)
        #print(ch)
    '''if cnt==2:
        break
    print(cnt,'번째 :',line)
    time.sleep(3)'''
    
sm.close()
#[][][]
