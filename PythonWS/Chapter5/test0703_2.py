# 프로그램 목적 : 재정의에 대한 실습

# 1) as를 이용한 재정의
import datetime as dt  # as를 쓰면 재정의 가능 -> C 언어의 typedef와 비슷
time = dt.datetime.now()  # dt는 라이브러리, datetime은 모듈 (일종의 헤더파일)
hour = dt.datetime.now().hour
# 2018-07-03 16:18:42.321324 와 같은 형식으로 출력
print(hour)  # 시간을 추출하는 방법 1
print(time.hour)  # 시간을 추출하는 방법 2
print(time)  # 전체 시간을 출력

# 2-1) import의 의미
import random  # 이렇게 하면 random이라는 라이브러리 내의 모든 모듈 사용가능
coin = random.choice(['앞면', '뒷면'])
dice = random.randrange(1, 7, 1)  # 주의) choice 이외에 random 소속된 함수를 쓰면 에러!

# 2-2) from, import의 의미
from random import choice  # 이렇게 하면 random이란 부분을 생략가능!
# 모듈을 불러옴 -> using namespace std;와 유사
coin = choice(['앞면', '뒷면'])  # 주의) coin = random.choice()로 쓰면 에러!
# dice = random.randrange(1, 7, 1)  # 주의) choice 이외에 random 소속된 함수를 쓰면 에러!