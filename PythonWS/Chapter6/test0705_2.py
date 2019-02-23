#  프로그램 목적: 반복문을 응용한 프로그램 만들기

# 1) 입력받은 단의 구구단을 출력하는 프로그램
user = int(input('원하는 단을 입력해주십시오 : '))

# a. for 문을 이용한 구현
for i in range(1, 10):  # 초기화, 조건지정, 증감연산
    print('{:#d} x {:#d} = {:#d}'.format(user, i, user*i))  # 구구단 처리

# b. while 문을 이용한 구현
i = 1  # 초기화
while i <= 9:  # 조건지정
    print('{:#d} x {:#d} = {:#d}'.format(user, i, user * i))  # 구구단 처리
    i += 1  # 증감연산
print('=' * 50)

# 2) 구구단 모든 단 출력 -> 중첩 for 문
# a. for 문을 이용한 구현
for i in range(1, 10):  # 외부 for 문 -> 단 제어
    print('<{:#d}단 출력>'.format(i))
    for j in range(1, 10):  # 내부 for 문 -> 구구단 제어
        print('{:#d} x {:#d} = {:#d}'.format(i, j, i * j))

# b. while 문을 이용한 구현
i = 1  # 초기화
j = 1  # 초기화
while i <= 9:
    print('<{:#d}단 출력>'.format(i))
    while j <= 9:
        print('{:#d} x {:#d} = {:#d}'.format(i, j, i * j))
        j += 1
    i += 1
    j = 1  # 주의) j를 다시 쓰기 위해서는 반드시 초기화 해주어야 함

# 3) 팩토리얼의 값 구하기 -> 재귀호출 || 반복문
n = int(input('팩토리얼 수를 입력해주십시오 : '))
fact = 1  # 결과값 저장을 위한 변수
for i in range(1, n + 1):
    fact *= i
print('{:#d}! = {:#d}'.format(n, fact))

# 4) 패스워드 체크
pw = 'python'
userPw = ''
while userPw != pw:
    userPw = input('패스워드를 입력해주십시오 : ')
print('로그인이 성공하였습니다.')
# 참고) while: 반복횟수 지정되지 않은 경우, for: 반복횟수가 지정된 경우