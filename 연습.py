while True:
    st=input('문자열을 입력하면 가운데 문자를 찾아드립니다!')
    t=int(len(st)/2)
    temp=st[t]
    print('당신이 입력한 문자열은',st,'이고 가운데 문자는',temp,'입니다.')




while True:
    st=input('문자열을 입력하면 가운데 문자를 찾아드립니다!')
    print('당신이 입력한 문자열은',st,'이고 전체 문자열의 길이는',len(st),'입니다.')

    if len(st)%2==0:
        t=int(len(st)/2)
        run=st[t-1]+st[t]
    else:
        t=int(len(st)/2)
        run=st[t]


    print('가운데 문자는',run,'입니다.')
