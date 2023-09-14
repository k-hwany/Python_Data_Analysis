# + 연산자를 사용하면 2개의 리스트를 합칠수 있다.
# 합친 새 리스트 생성 후 요소의 값을 3으로 나누었을 때 1인 요소들만 출력

listA=['A','B','C']
listB=['D','E','F']

listAll = listA + listB

for i in range(len(listAll)):
    if i % 3 == 1:
        print(listAll[i])