# 프로그램 목적: 10진수 숫자를 2진수로 변환하는 프로그램 작성
# 학번: 12131819, 이름: 육동현


def separate_decimal(param):  # 십진수를 '정수부'와 '소수부'로 나눔
    dec_integer = int(param)  # 십진수의 정수부 추출
    dec_fraction = param - dec_integer  # 십진수 소수부 추출
    return dec_integer, dec_fraction  # 처리결과 반환


def converse_integer(param):  # 십진수의 '정수부'를 이진수로 전환
    result = list()  # 결과값을 저장할 리스트 생성
    temp = param
    while temp != 0:
        remainder = temp % 2  # 나머지를 구함
        result.append(str(remainder))  # 결과 리스트에 추가
        temp //= 2  # 정수 나누기 2를 해서 결과저장
    result.reverse()  # 리스트 순서를 반전시킴
    return result  # 결과값 반환


def converse_fraction(param):  # 십진수의 '소수부'를 이진수로 전환
    result = list()  # 결과값을 저장할 리스트 생성
    temp = param
    result.append('.')  # 소숫점(.)을 표현하기 위한 처리
    while temp != 0:  # temp가 0이 아닌 동안 루프수행
        temp *= 2  # 곱하기 2씩 해나감
        result.append(str(int(temp)))  # 나온 캐리를 리스트에 저장
        temp -= int(temp)  # 캐리를 빼고 다시 루프수행
    return result  # 결과값 반환


# 사용자로부터 십진수를 입력받음
userInput = float(input('이진수로 변환할 십진수를 소숫점을 포함하여 입력해주십시오 : '))
print('십진수 분해결과 : {}'.format(separate_decimal(userInput)))  # 분해결과 출력
integer, fraction = separate_decimal(userInput)  # 분해된 정수부와 소수부를 변수에 저장

# 정수부를 변환하는 처리
print('십진수 정수부 변환결과 : ', end='')
for i in converse_integer(integer):
    print(i, end='')
print('(2)')  # 진법을 표시하기 위한 처리

# 소수부를 변환하는 처리
print('십진수 소수부 변환결과 : 0', end='')
for i in converse_fraction(fraction):
    print(i, end='')
print('(2)')  # 진법을 표시하기 위한 처리

# 최종결과를 출력하는 처리
print('최종 이진수 변환결과 : ', end='')
for i in converse_integer(integer):  # 이진수 정수부를 출력
    print(i, end='')
for i in converse_fraction(fraction):  # 이진수 소수부를 출력
    print(i, end='')
print('(2)', end='')