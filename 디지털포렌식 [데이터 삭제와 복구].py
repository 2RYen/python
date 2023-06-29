source={'100':'김민주','300':'박민주','400':'허민주','500':'차민주'}   # {'주소':'데이터'} 0으로 리셋하면 있는 것처럼 보이지만 없다.
erase_item={}

'''for k in range(5):
    key_in=input('데이터가 저장되는 주소를 입력하세요')
    data=input('주소에 저장될 데이터를 입력하세요')
    source[key_in]=data
    print(source)'''

key_in=input('삭제 시킬 데이터의 주소를 입력하세요')
erase_item[key_in]=source[key_in]

source.pop(key_in)
print('원시 데이터 : ', source)
print('삭제 데이터 : ', erase_item)

key_in=input('복구 시킬 데이터의 주소를 입력하세요')
source[key_in]=erase_item[key_in]
print('원시 데이터 : ', source)
