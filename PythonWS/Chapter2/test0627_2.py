# 프로그램 목적 : 외부입력 연습

# 주의) 기본적으로 입력함수는 문자열로 인식
a = input("첫번째 정수를 입력해주십시오 : ")  # input()은 입력함수이다!
b = input("두번째 정수를 입력해주십시오 : ")
c = a + b
print(type(c))
print(a, '+', b, '=', c, '\n')  # input()의 입력값은 문자열이 디폴트 값임에 유의하자!

# 정상적인 코드로 바꾼 경우 -> int()를 이용하여 명시적 형변환을 수행
a = int(input("첫번째 정수를 입력해주십시오 : "))  # int()는 명시적 형변환
b = int(input("두번째 정수를 입력해주십시오 : "))
c = a + b
print(type(c))
print('{:#d} + {:#d} = {:#d}\n'.format(a, b, c))

# 도전문제
name = input('이름을 입력하시오 : ')
print(name, '씨, 안녕하세요?')
print('파이썬에 오신 것을 환영합니다.')
num1 = int(input('첫 번째 정수를 입력하시오 : '))
num2 = int(input('두 번째 정수를 입력하시오 : '))
ans = num1 + num2
print(num1, '과', num2, '의 합은', ans, '입니다.')

# 원의 넓이를 구하는 프로그램
radius = float(input('원의 반지름의 길이를 입력하시오 : '))
area = 3.14 * pow(radius, 2)
print('반지름의 길이가 \'{:#.2f}\'인 원의 면적은 \'{:#.2f}\'입니다.\n'.format(radius, area))