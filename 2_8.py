### 반복문 ###

# for 문과 문자열 조작

# 문자열.split(sep) - 문자열을 분리하여 리스트형을 만들어주는데, sep의 기본값은 공백
# 문자열.upper()    - 문자열 목록을 모두 대문자로 변환
# 문자열.lower()    - 문자열 목록을 모두 소문자로 변환
# 문자열.replace(oldstr,newstr) - 특정 문자열 치환
# 'joinstr'.join(iterable) - 반복되는 요소인 iterable(리스트, 튜플 등)에 대하여 'joinstr'문자열을
                            # 사용하여 결합된 결과를 반환
                            
mystring = 'life is an egg'
mylist=mystring.split()  # 공백을 기준으로 리스트형으로 변환

for idx in range(len(mylist)):
    if idx %2==0:
        mylist[idx] = mylist[idx].upper()
    else:
        mylist[idx] = mylist[idx].lower()
        
print('join() 함수를 이용하여 문자열 합치기')
result = '#'.join(mylist)

print('결과 : ', result)


# while 문 사용  # 커피 판매점

coffee = 3
price = 2000

print("판매 가능한 커피 잔량 : %d" % (coffee))
print("단가 : %d원" % (price))

while True:
    money = int(input("돈을 넣어주세요 : "))
    
    if money == price:
        print("커피를 판매합니다.")
        coffee -= 1
    elif money > price:
        print("거스름돈 {}를 주고, 커피를 팝니다.".format(money-price))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고, 커피를 팔지 않습니다.")
    
    print("남은 커피 양은 {}개 입니다.".format(coffee))
    
    if coffee==0:
        print("커피가 없습니다. / 판매를 중단합니다.")
        break