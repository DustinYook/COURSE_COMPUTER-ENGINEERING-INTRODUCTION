# 프로그램 설명: 함수가 정의된 피참조 파일
def add_two(num1, num2):
    return num1 + num2


if '__name__' == '__main__':
    print(add_two(1, 2))