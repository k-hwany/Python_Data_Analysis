### 집합 자료형 ###
# 리스트 list()    데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 []
# 튜플 tuple()     데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 ()
# 딕셔너리 dict()  키 X, 값 O   , 순서 없음, 요소개수len() 사용, 사용기호 {}


tuple01 = (10,20,30)  
tuple01 = tuple01 + (40, )   # 튜플은 (40)으로하면 정수로 인식하여 콤마(,)를 추가해야 함
print('tuple : ',tuple01)

tuple02 = 10,20,30,40   # 단순 콤마 연결

mylist=[10,20,30,40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print("component equal")
else:
    print("component not equal")
    

tuple04=(10,20,30)
tuple05=(40,50,60)

print('+ 연산자는 2개의 튜플을 합치는 역할을 합니다.')
tuple06 = tuple04 + tuple05
print(tuple06)


print('* 연산자는 튜플을 지정한 정수만큼 반복시키는 역할')
tuple07=tuple04*3
print(tuple07)


print('튜플을 사용하면 변수들을 swap 시킬수 있음')
a,b=11,22
a,b=b,a
print('a= ',a,'b=',b)


#슬라이싱
tuple08=(11,22,33,44,55,66)
print(tuple08[1:3])
print(tuple08[3:])

#튜플을 요소의 개수를 늘리거나 줄일수는 있지만, 값을 수정하는 것은 불가능
# tuple08[0] = 100  <-- TypeError