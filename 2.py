# 파이썬 다루기

###### 데이터의 형 변환 ######
# str1='100'
# str2='200'
# str3='12.345'

# int1=int(str1)
# int2=int(str2)
# float1=float(str3)

# print(int1==str)

# sum = int1+int2
# print(sum)
# float2=float1+35.2
# print(float2)

# print(type(str1))
# print(type(int1))
# print(type(float1))




###### 입출력 함수 사용 ########
# name = input('이름 : ')
# age = int(input('나이 : '))

# # %s - 문자열 치환, %c - 1개 문자 치환, %d - 정수 값 치환, %f 실수 값 치환

# print('이름 : %s' % (name))
# print('나이 : %d' % (age))



####### format() 함수 - 문자열 안의 특정 위치에 특정 값 삽입 #######
# coffee = 3   # 판매 가능 커피 수 
# price = 2000 # 커피 가격

# print("우리 매장에 커피 {} 잔이 있습니다".format(coffee))

# money = int(input("돈을 넣어주세요 : "))
# print("{}원을 입금하셨습니다.".format(money))


# # Example 2 
# change = money - price
# print("거스름돈은 {}원이며, 커피 {}잔을 구매하셨습니다.".format(change, 1))
# print("남은 커피양은 {}잔 입니다.".format(coffee-1))


#### 조건문 ####

# salary = int(input('월급 : '))
# income =0 #연봉
# tax =0  # 세금

# # 연봉구하기
# if salary >= 500:
#     income = 12*salary
# else:
#     income = 13*salary
    
# # 세금 구하기
# if income >= 10000:
#     tax=0.2*income
# elif income >= 7000:
#     tax = 0.15*income
# elif income >= 5000:
#     tax=0.12*income
# elif income >=1000:
#     tax=0.1*income
# else:
#     tax =0
    
# print('월급 : %d' % (salary))
# print('연봉 : %.2f' % (income))
# print('세금 : %.2f' % (tax))



### 집합 자료형 ###
# 리스트 list()    데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 []
# 튜플 tuple()     데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 ()
# 딕셔너리 dict()  키 X, 값 O   , 순서 없음, 요소개수len() 사용, 사용기호 {}

# somelist = ['A','B','C','D','E','F','G']
# print(somelist)
# print(somelist[4])  # 4번째 , 0부터 시작
# print(somelist[-2])  # 뒤에서 2번째
# print(somelist[1:4]) # 1번 부터 4번 까지
# print(somelist[4:])  # 4번부터 끝까지

# length = len(somelist)    # 전체 길이 구함
# print('홀수만 출력')
# print(somelist[1:length:2])  # 1번부터 step(간격)을 2로 지정
# print('짝수만 출력')
# print(somelist[0:length:2])   # 0번부터 간격을 2로 지정
# print('3 배수 출력')
# print(somelist[0:length:3])   # 0번 부터 간격을 3으로 지정


tuple01 = (10,20,30)  
tuple01 = tuple01 + (40, )   # 튜플은 (40)으로하면 정수로 인식하여 콤마(,)를 추가해야 함
print('tuple : ',tuple01)