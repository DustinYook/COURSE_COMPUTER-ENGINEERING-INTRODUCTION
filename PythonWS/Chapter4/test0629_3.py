# 프로그램 목적 : 나이를 구하는 프로그램
import time  # import는 모듈을 불러오는 명령어 -> C 언어의 #include <limit.h> 등과 유사
now = time.time()  # time()은 처리를 시작한 시간을 저장
processStart = now  # 프로그램 처리 시작시간
thisYear = int(1970 + now // 365 // 24 // 60 // 60)  # 일 -> 시간 -> 분 -> 초
# 다른 표현방법 : now // (365 * 25 * 3600)
print('올해는', thisYear, '년 입니다.')
age = int(input('몇 살인지 입력해 주십시오 : '))
print('2050년에는 ', (2050 - thisYear) + age, '살이 됩니다.', sep='')
processEnd = time.time()  # 여기에서는 시간이 경과되어 앞의 time()과는 다름
print('프로그램 처리시간은 ', (processEnd - processStart), ' ms 입니다', sep='')  # 프로그램 처리시간