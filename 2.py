# 파이썬 다루기

# 데이터의 형 변환
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




# 입출력 함수 사용
# name = input('이름 : ')
# age = int(input('나이 : '))

# # %s - 문자열 치환, %c - 1개 문자 치환, %d - 정수 값 치환, %f 실수 값 치환

# print('이름 : %s' % (name))
# print('나이 : %d' % (age))



# format() 함수 - 문자열 안의 특정 위치에 특정 값 삽입
# coffee = 3   # 판매 가능 커피 수 
# price = 2000 # 커피 가격

# print("우리 매장에 커피 {} 잔이 있습니다".format(coffee))

# money = int(input("돈을 넣어주세요 : "))
# print("{}원을 입금하셨습니다.".format(money))


# # Example 2 
# change = money - price
# print("거스름돈은 {}원이며, 커피 {}잔을 구매하셨습니다.".format(change, 1))
# print("남은 커피양은 {}잔 입니다.".format(coffee-1))