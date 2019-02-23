# 프로그램 목적: 리스트에 대한 기초실습 1
# 주의) 리스트:[] vs 딕셔너리/셋:{} vs 튜플:()
# 참고) 사용하지 않을 코드 주석 -> 함수만들고 호출하지 않으면 됨

# 중요) 배열은 고정크기 vs 리스트는 가변크기 -> 파이썬에 배열없음
l1 = list()  # l1 = []와 같은 의미, 단지 함수로 리스트를 생성한 것
print(type(l1))

# 1) append()의 사용법 -> 삽입방법 #1
l1.append('A')  # 리스트의 맨 끝 부분에 자료추가
l1.append('B')  # l1은 객체명 -> 도트 연산자를 통해 멤버 볼 수 있음
l1.append('E')
print(l1)  # 결과값: A B E

# 2) insert()의 사용법 -> 삽입방법 #2
l1.insert(2, 'C')  # 리스트의 2번째 인덱스 위치에 삽입
l1.insert(3, 'D')  # 리스트의 3번째 인덱스 위치에 삽입
print(l1)  # 결과값: A B C D E

# 3) reverse()의 사용법
l1.reverse()  # 리스트를 거꾸로 뒤집음
print(l1)  # 결과값: E D C B A
l1.reverse()  # 리스트를 거꾸로 뒤집음
print(l1)  # 결과값: A B C D E

# 참고) reverse()의 내부구현
temp = l1.copy()  # 얕은복사: copy()를 안쓰면 래퍼런스가 됨에 유의!
l2 = list()
for i in range(len(temp)):
    popped = temp.pop()
    l2.append(popped)
print(l2)

# 4) remove()의 사용법 -> 삭제방법 #1
l1.remove('E')  # 주의) remove(첨자)로 쓰면 문법적오류!
print(l1)  # 결과값: A B C D
l1.remove(l1[3])  # 주의) 인덱스에 따라 제거하고 싶으면 이 형식을 사용해야 함!
print(l1)  # 결과값: A B C
# 리스트에서 위치 또는 내용으로 제거하는 방법 헷갈리지 않도록 주의할 것!

# 5) pop()의 사용법 -> 삭제방법 #2
temp = l1.pop()  # 디폴트로는 가장 뒷 부분의 원소가 튀어나옴
print(temp)  # 결과값: C
print(l1)  # 결과값: A B
temp = l1.pop(0)  # 0번째 인덱스 원소가 튀어나옴
print(temp)  # 결과값: A
print(l1)  # 결과값: B
# remove(): 그냥 날려버림 vs pop(): 값을 가지고 옴 -> 차이 구분!

# 6) del 키워드 사용법 -> 삭제방법 #3
del l1[0]  # l1의 0번째 인덱스 원소 삭제 <=> l1.remove(l1[0])
print(l1)  # 결과값: [ ]