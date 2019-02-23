# 프로그램 목적: 리스트, 딕셔너리/셋, 튜플
# 주의) 리스트:[] vs 딕셔너리/셋:{} vs 튜플:()

# 1) 리스트 -> 가변크기, 중복제거 없음
a = [1, 2]
print(type(a), a)

# 2) 셋 -> 자동 중복제거
a = {1}
print(type(a), a)

# 3) 딕셔너리
a = {1: 2}
print(type(a), a)

# 4) 튜플 -> 읽기전용(수정불가)
a = (1, 2)
print(type(a), a)

# 2개 이상을 한 변수로 받으면 튜플로 인식
a = 10, 20
b = 10, 20, 30
print(type(a), a)  # <class 'tuple'> (10, 20)
print(type(b), b)  # <class 'tuple'> (10, 20, 30)
# b[0] = 100  # 튜플은 읽기전용 (배정문 불가)
# 주의) 2개의 변수를 2개의 변수로 받는 것은 튜플이 아님
a, b = 10, 20
print(type(a), a, type(b), b)

# 튜플의 원소 접근하는 방법 -> 리스트와 동일
a = '12131819', '육동현', 100
print(type(a), a)  # <class 'tuple'> ('12131819', '육동현', 100)
print(type(a[0]), a[0])  # <class 'str'> 12131819
print(type(a[1]), a[1])  # <class 'str'> 육동현
print(type(a[2]), a[2])  # <class 'int'> 100
student_id, name, score = a  # 튜플은 여러 변수로 나눠 받아올 수 있음
print('학번 :', student_id)
print('이름 :', name)
print('점수 :', score)