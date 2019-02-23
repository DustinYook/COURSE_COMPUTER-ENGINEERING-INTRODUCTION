# 프로그램 목적: random 모듈을 이용한 프로그램

# 1) 동전 던지기 프로그램
import random  # random 내장모듈을 사용하기 위함
print('이 프로그램은 동전던지기를 수행하는 프로그램입니다.')
print('=' * 50)  # 경계선을 그어주는 역할
coin = random.randrange(2)
# randrange(시작, 끝, 간격) -> 시작의 초기값은 0, 간격의 초기값은 1
if coin % 2 == 0:
    print('동전은 \'앞면\'이 나왔습니다.')
else:
    print('동전은 \'뒷면\'이 나왔습니다.')
print('=' * 50)

# 2) 주사위 던지기 프로그램
# import random
print('이 프로그램은 주사위 던지기를 수행하는 프로그램입니다.')
print('=' * 50)  # 경계선을 그어주는 역할
myDice = random.randrange(1, 7, 1)  # randrange(시작, 끝, 간격)
yourDice = random.randrange(1, 7, 1)
# 주의) 시작은 '이상', 끝은 '미만'임에 유의하도록 한다!
if myDice > yourDice:
    print('내가 이겼습니다.')
elif myDice == yourDice:
    print('비겼습니다.')
else:
    print('내가 졌습니다.')
print('=' * 50)

# 3) 랜덤으로 1부터 10 사이의 홀수와 짝수를 출력하는 프로그램
# import random
odd = random.randrange(1, 11, 2)
print('임의로 추출된 홀수는 \'{}\'입니다.'.format(odd))
even = random.randrange(2, 11, 2)
print('임의로 추출된 짝수는 \'{}\'입니다.'.format(even))