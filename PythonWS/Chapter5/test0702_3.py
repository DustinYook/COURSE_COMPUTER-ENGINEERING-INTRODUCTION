# 프로그램 목적: time 모듈을 이용하여 윤년을 계산하는 프로그램
import time
now = time.time()  # 1970년 1월 1일부터 경과한 시간을 ms 단위로 받음
timePass = int(now // 365 // 24 // 60 // 60)
thisYear = timePass + 1970
if ((thisYear % 4 == 0) and (thisYear % 100 != 0)) or (thisYear % 400 == 0):
    print('{:#d}년은 윤년입니다.'.format(thisYear))
else:
    print('{:#d}년은 윤년이 아닙니다.'.format(thisYear))
# 그 동안 배운 것을 항상 반복 사용하는 연습을 하는 것이 중요하다!