# 1) 종달새 노래
import random  # random 라이브러리를 포함
# time = random.randrange(0, 25, 1)
# 주의) randrange(시작, 끝, 간격)은 시작 이상, 끝 미만이나
#       randint(시작, 끝, 간격)은 시작 이상, 끝 이하임에 유의!
time = random.randint(1, 24)  # randint(시작, 끝) <=> 1 이상, 24 이하의 임의의 수 추출
weather = random.choice(['화창', '흐림'])  # choice()는 리스트 안에서 하나를 임의로 택하는 함수
if (6 <= time <= 9) or (14 <= time <= 16):  # 파이썬은 C 언어와는 다르게 이런 형식이 가능! [범위검색]
    if weather == '화창':
        print('종달새가 웁니다')

# 2) 로그인 프로그램
# 참고) C 또는 JAVA에서는 '=='을 통해 문자열 비교 불가!
id = input('아이디를 입력하십시오 : ')
pw = input('패스워드를 입력하십시오 : ')
if id == 'python' and pw == '123':
    print('성공적으로 로그인 되었습니다.')

# 3) 패널티킥을 구현한 프로그램
import random
computer = random.choice(['left', 'middle', 'right'])
move = input('어디를 수비하시겠습니까? (left/middle/right) : ')
print('당신의 선택은 {}입니다.'.format(move))
print('컴퓨터의 선택은 {}입니다.'.format(computer))
if computer == move:
    print('성공적으로 방어했습니다.')
else:
    print('방어에 실패하였습니다.')

# 3) 가위바위보를 구현한 프로그램
import random
choices = ['가위', '바위', '보']
computer = random.choice(choices)
myChoice = input('나의 선택을 입력해주십시오 : ')
if computer == '가위':
    if myChoice == '가위':
        print('무승부')
    elif myChoice == '바위':
        print('승리')
    else:
        print('패배')
elif computer == '바위':
    if myChoice == '가위':
        print('패배')
    elif myChoice == '바위':
        print('무승부')
    else:
        print('승리')
else:
    if myChoice == '가위':
        print('승리')
    elif myChoice == '바위':
        print('패배')
    else:
        print('무승부')
print('당신의 선택은 {}입니다.'.format(myChoice))
print('컴퓨터의 선택은 {}입니다.'.format(computer))
# 반복문 배우고 나면 3전 2선승제 구현해보기!