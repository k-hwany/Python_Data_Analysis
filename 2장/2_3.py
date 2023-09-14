###### format() 함수 - 문자열 안의 특정 위치에 특정 값 삽입 #######
coffee = 3   # 판매 가능 커피 수 
price = 2000 # 커피 가격

print("우리 매장에 커피 {} 잔이 있습니다".format(coffee))

money = int(input("돈을 넣어주세요 : "))
print("{}원을 입금하셨습니다.".format(money))


# Example 2 
change = money - price
print("거스름돈은 {}원이며, 커피 {}잔을 구매하셨습니다.".format(change, 1))
print("남은 커피양은 {}잔 입니다.".format(coffee-1))

