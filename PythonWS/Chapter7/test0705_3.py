# 프로그램 목적: 함수에 대한 기초실습


def prints():  # 함수정의
    print('123')
    print('ABC')
    print('우리나라')


prints()  # 함수호출
prints()
prints()
# 함수의 유용성: 가독성향상(작업에 명칭부여), 유지보수용이


def func(num1, num2):  # 함수는 여러 개의 인자를 받을 수 있다
    result = num1 + num2
    return result  # 함수는 값 반환을 할 수 있다


print(func(10, 20))  # 반환 받은 값을 바로 출력하는 방법
result2 = func(10, 20)
print(result2)  # 값을 일단 저장 후 출력하는 방법


def calculate_area(r):  # 함수는 인자를 받아 처리
    area = 3.14 * r ** 2
    return area


radius = float(input('원의 반지름을 입력해주십시오 : '))
print(calculate_area(radius))