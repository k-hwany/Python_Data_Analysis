# 3. 정수를 1개 입력받아 짝수면 제곱, 홀수면 3제곱 출력하는 프로그램

number = int(input("숫자를 입력하세요 : "))

if number % 2 ==0:
    print(number**2)
else:
    print(number**3)
