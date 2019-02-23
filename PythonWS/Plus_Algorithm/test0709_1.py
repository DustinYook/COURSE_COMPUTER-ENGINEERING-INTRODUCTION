# 프로그램 목적: 기본적인 알고리즘 구현


def maximum1(a):  # 최대값 구하기 1
    result = a[0]
    for element in a:
        if result < element:
            result = element
    return result


def maximum2(a):  # 최대값 구하기 2
    result = a[0]
    for index in range(len(a)):
        if result < a[index]:
            result = a[index]
    return result


li = [12, 8, 13, 5, 11]
print(maximum1(li), maximum2(li))


score = int(input('점수를 입력해주십시오 : '))  # 평점 구하기
grade = ''
if 100 >= score >= 90:  # 파이썬은 범위검색 가능
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print('학점은 {} 입니다.'.format(grade))