# 프로그램 목적: 지역변수와 전역변수에 대한 실습


def calc_area():  # 밖에서 지역의 r은 invisible
    result = 3.14 * 10 ** 2  # 핵심) 여기에서 result는 calc_area()의 지역변수
    # print(result)  # 여기에서는 정상적으로 계산됨
    return result


result = 0  # 핵심) 여기에서 result는 main()의 지역변수
area = calc_area()
print(result)  # 핵심) 여기에서는 0으로 결과값이 찍힘
# 이유: calc_area()의 result와 전혀 별개이기 때문 (일종의 동명이인)


def calculate_area(radius):
    global area  # 핵심) 전역변수로 선언!
    area = 3.14 * radius ** 2
    return  # blank return

area = 0  # 여기는 위의 area와 연동되어 움직임
r = float(input('원의 반지름의 길이를 입력해주십시오: '))
calculate_area(r)  # 결과값이 아까와는 다르게 제대로 찍힘
print(area)
# 전역변수를 사용하면 가독성 떨어짐 -> 내가 모르는 사이에 값 변경될 수 있기 때문