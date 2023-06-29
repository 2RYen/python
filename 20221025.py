# algorithm 알고리즘(듬) : 어떤 문제를 해결하기 위한 절차와 방법
# algorithm -> coding (language) python C fortran javascript)


a=[3,5,7,9,11]
b=[1,2,6,8]
c=[0 for cnt in range(len(a)+len(b))]
asp=0
bsp=0
csp=0

while len(a)+len(b) != asp+bsp:                                                # True: #!= len(c) /
    if a[asp]<b[bsp]:
        c[csp]=a[asp]
        if len(a) != asp+1:
            asp=asp+1
    else:
        c[csp]=b[bsp]
        if len(b) != bsp+1:
            bsp=bsp+1
        if len(a)==asp+1:
            for k in range(bsp, len(b)+1):
                c[csp]=b[k]
                csp=csp+1
        elif len(b)==bsp+1:
            for k in range(asp, len(a)+1):
                c[csp]=a[k]
                csp=csp+1


    csp=csp+1
    print(c)
