name=['은비', '아영', '소린', '종은', '서현']
phone=['01085793680', '01033403093', '01074770867', '01077520904', '01067106196']

while True:
    irum=input('이름을  입력하시면 전화번호를 알려드립니다!(입력종료:end)')
    if irum=='end' or irum=='END':
        break
    no=name.index(irum)
    po=phone[no]



    print(irum,'은',po,'입니다.')
