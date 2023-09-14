# 입금한 금액만큼 한번에 커피 여러잔을 판매할 수 있도록 본문에서 사용한 coffeeSales.py 파일 수정

# 문제 난이도 자발적 Up~~ 먼저 하루에 판매할 커피 양을 정할 수 있다.
# 이유 - 3 잔으로 지정하면 if 문을 사용하면 금방 끝나기에 판매할 커피가 100일 경우 
#           조건문 100개가 아닌 다른 방법을 생각하기 위함

coffee = int(input("오늘 판매할 커피 잔을 입력하세요 : "))
price = 2000

print("판매 가능한 커피 잔량 : %d" % (coffee))
print("단가 : %d원" % (price))

while True:
    money = int(input("돈을 넣어주세요 : "))
    
    for x in range(coffee): 
        if money == price:
            print("커피를 판매합니다.")
            coffee -= 1
            break
        elif money > price:
            if money//price == x:    
                print("커피를 판매합니다. 거스름돈은 {}원 입니다.".format(money-price*x))
                coffee -= x
                break
        else:
            print("금액이 부족합니다.")
            break
        
        
    print("남은 커피 양은 {}개 입니다.".format(coffee))
    
    if coffee==0:
        print("커피가 모두 판매되었습니다. / 판매를 중단합니다.")
        break