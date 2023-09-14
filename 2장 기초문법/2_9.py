# 리스트 컴프리헨션 (list comprehension)
# - 반복(iterable)할 수 있는 오브젝트(리스트, 튜플 등)를 생성하기 위한 유용한 문법

mylist01=list(onedata for onedata in range(1,6))
print(mylist01)

mylist02=list(10 * onedata for onedata in range(1,6))
print(mylist02)

mylist03=[3,4,6,2]
result = [idx**2 for idx in mylist03 if idx%2==0]   # **2  2제곱 이란 뜻 / 짝수인 요소를 제곱하여 출력
print(result)