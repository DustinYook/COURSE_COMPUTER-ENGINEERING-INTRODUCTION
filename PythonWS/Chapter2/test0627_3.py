# 프로그램 목적 : 진법변환 -> format 함수 잘 알아두기!

# 1) 함수를 이용하여 진법을 변환하는 방법
num = int(input('10진수 표현을 입력해주십시오 : '))
print('2진수 표현 : {}'.format(bin(num)))  # bin()이라는 함수는 2진법 표현으로 전환
print('8진수 표현 : {}'.format(oct(num)))  # oct()라는 함수는 8진법 표현으로 전환
print('16진수 표현 : {}'.format(hex(num)))  # hex()라는 함수는 16진법 표현으로 전환
print('=' * 30)

# 2) 형식지정자를 이용하여 진법을 변환하는 방법
print('2진수 표현 : {:#b}'.format(15))  # {:#b}는 2진법으로 찍어주는 형식지정자
print('8진수 표현 : {:#o}'.format(15))  # {:#o}는 8진법으로 찍어주는 형식지정자 -> C 언어의 %o와 동일
print('16진수 표현 : {:#x}\n'.format(15))  # {:#x}는 16진법으로 찍어주는 형식지정자 -> C 언어의 %x와 동일
# 교수님의 조언) 배운 것을 프로그램으로 만들 방법이 없을까 고민해봐야 함!
# 직접 해보기) 54.12를 2진법, 8진법, 16진법으로 변환하는 함수만들기

# 3) format 함수에 대한 심화학습
num1 = int(input('첫 번째 정수를 입력해주십시오 : '))
num2 = int(input('두 번째 정수를 입력해주십시오 : '))
result = num1 + num2
print(result, '=', num1, '+', num2)  # 원래라면 이렇게 출력해야 하나 헷갈림
print('{} = {} + {}\n'.format(result, num1, num2))  # format()을 쓰면 보다 직관적으로 표현가능

# 4) print()는 기본적으로 숫자를 넣으면 10진수의 형식으로 출력함에 유의!
print(15)  # 10진수 -> 10진수
print(0b1111)  # 2진수 -> 10진수
print(0o17)  # 8진수 -> 10진수
print(0xf)  # 16진수 -> 10진수
print('=' * 30)

# 5) int(param1, param2)를 이용하는 방법
#    param1은 피연산수를 의미하는 인자 -> 반드시 문자열로 받아야 함!
#    param2는 인식할 진법을 나타내는 인자
# print(int(0b1111, 2))  # int() can't convert non-string with explicit base -> 2진법은 문자열로 인식!
# 문자열을 받아서 진법에 의해 숫자로 바꿀 때 쓰는 syntax
print(int('0b1111', 2))  # 2진법을 인식하여 10진법으로 출력
print(int('0o17', 8))  # 8진법을 인식하여 10진법으로 출력
print(int('0xf', 16))  # 16진법을 인식하여 10진법으로 출력
print('=' * 30)

# 6) bin(), oct(), hex()의 결과값은 문자열, int()의 결과값은 숫자
#    여기서 주의할 점은 int()는 디폴트로 10진수로 강제형변환을 수행한다
binary = bin(int('0b1111', 2))  # <class 'str'>
print(type(binary))
binary = int('0b1111', 2)  # <class 'int'>
print(type(binary))
print('=' * 30)
octal = oct(int('0o17', 8))  # <class 'str'>
print(type(octal))
octal = int('0o17', 8)  # <class 'int'>
print(type(octal))
print('=' * 30)
hexadecimal = hex(int('0xf', 16))  # <class 'str'>
print(type(hexadecimal))
hexadecimal = int('0xf', 16)  # <class 'int'>
print(type(hexadecimal))
print('=' * 30)