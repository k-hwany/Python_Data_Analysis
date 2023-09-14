# 2. 품목 이름과 수량과 단가를 입력받아 총 금액을 구하는 프로그램

name = input("품목 : ")
num = int(input("수량 : "))
price = int(input("단가 : "))

print('### 출력 결과 ### \n품목 : {} \n수량 : {} \n단가 : {} \n총 금액 : {}'.format(name,num,price,price*num))