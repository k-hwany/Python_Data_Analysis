### 집합 자료형 ###
# 리스트 list()    데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 []
# 튜플 tuple()     데이터중복가능, 순서있음, 요소개수len() 사용, 사용기호 ()
# 딕셔너리 dict()  키 X, 값 O   , 순서 없음, 요소개수len() 사용, 사용기호 {}

somelist = ['A','B','C','D','E','F','G']
print(somelist)
print(somelist[4])  # 4번째 , 0부터 시작
print(somelist[-2])  # 뒤에서 2번째
print(somelist[1:4]) # 1번 부터 4번 까지
print(somelist[4:])  # 4번부터 끝까지

length = len(somelist)    # 전체 길이 구함
print('홀수만 출력')
print(somelist[1:length:2])  # 1번부터 step(간격)을 2로 지정
print('짝수만 출력')
print(somelist[0:length:2])   # 0번부터 간격을 2로 지정
print('3 배수 출력')
print(somelist[0:length:3])   # 0번 부터 간격을 3으로 지정



intlist=[1,2,3,4,5,6,7,8,9,10]
result = sum(intlist)   # sum 함수를 사용하여 배열의 숫자 합을 구할 수 있다!
print(result)