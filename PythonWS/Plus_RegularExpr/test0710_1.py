# 프로그램 목적: 정규표현식에 대한 실습
import re  # 정규표현식을 사용하기 위한 저리

# ''' ''' 사이에 문자열을 넣으면 하나의 문자열로 인지
db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# 정규표현식(Regular Expression) -> re.findall(r'정규표현식', 대상)
# 1) 숫자형 패턴인식
num1 = re.findall(r'[0-9]', db)  # 숫자 한 자리만 잡아옴
print(num1)  # 출력결과: ['3', '4', '1', '2', ... ]
num2 = re.findall(r'[0-9]*', db)  # 공백(0번 반복) 또는 모든 숫자의 나열(여러번 반복)을 잡아옴
print(num2)  # 출력결과: ['3412', '', '', '', ... ]
num3 = re.findall(r'[0-9]+', db)  # 숫자가 한 번이상 반복되는 패턴을 인식
print(num3)  # 출력결과: ['3412', '123', '3834', ...]

# 2) 문자형 패턴인식
name1 = re.findall(r'[a-zA-Z]', db)  # 영어 대소문자 패턴 한 글자를 인식
print(name1)  # 출력: ['B', 'o', 'b', 'J', 'o', 'n', 'n', 'y']
name2 = re.findall(r'[A-Z][a-z]+', db)  # 영어 대소문자 패턴 한 글자 이상을 인식
print(name2)  # 출력: ['Bob', 'Jonny', ...]
name3 = re.findall(r'[a-z]+', db)  # 이렇게 하면 소문자만 인식되어 주의
print(name3)  # 출력: ['ob', 'onny', ...]
name4 = re.findall(r'[a-zA-Z]*', db)  # 이렇게 하면 공백 또는 모든 문자의 나열의 패턴을 인식
print(name4)  # 출력: ['', '', '', '', '', '', '', '', 'Bob', ...]

# 3) 특정 문자열을 포함 또는 제외하는 패턴인식 방법
name5 = re.findall(r'[T][a-z]+', db)  # 이름이 'T'로 시작하는 문자열 패턴인식
print(name5)  # 출력: ['Tony']
name6 = re.findall(r'[A-SU-Z][a-z]+', db)  # 이름이 'T'로 시작하지 않는 문자열 패턴인식
print(name6)  # 출력: ['Bob', 'Jonny', 'Kate', 'Peter', 'Alice', 'Kerry']
name7 = re.findall(r'[^T][a-z]+', db)  # 주의) 이렇게 하면 안됨!
print(name7)  # 출력: ['Bob', 'Jonny', 'Kate', 'ony', 'Peter', 'Alice', 'Kerry']