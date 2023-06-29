# 함수: 특정 목적을 수행하는 코드의 집합  함수 -> 객체(object) / 함수: 내부(장) 함수, 외부함수
# 내부함수(Internal function): 언어가 설계될 때 만들어진 함수 / 외부함수(external function):  사용자가 필요할 때 만들어 쓰는 함수

'''while True:
    digit=int(input('숫자를 입력하시면 절댓값을 구해드립니다!')

#    ab=abs(digit)

    print('{}의 절댓값은 {}입니다.'.format(digit,abs(digit)))
              '''

def minju(digit):
    if digit<0:
        ret=digit*(-1)
    else:
        ret=digit

    return ret

def sungmin(what):
    for element in what:
        if not element:
            return False
        return True


# Boolean algibra 부울대수 = bool
