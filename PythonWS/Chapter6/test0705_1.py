# 프로그램 목적: 반복문 기초학습

# 1) range(시작, 끝, 간격) -> '시작'이상, '끝'미만, '간격'단위증가
for i in range(3):
    print('방문을 환영합니다!')

# 2) in [리스트] -> 리스트의 모든 내용을 출력
for i in ['강아지', '고양이', '망아지', '송아지']:
    print(i)

for i in [3, 2, 1]:  # 3부터 1까지 거꾸로 출력
    print(i)  # 출력결과: 3 2 1

# 주의) C 언어의 for(i=3, i>0; i--)와 같은 표현
for i in range(3, 0, -1):  # 3부터 1까지 거꾸로 출력
    print(i)  # 출력결과: 3 2 1

# 3) while과 for의 전환
i = 1  # 초깃값
result = 0  # 결과저장변수
while i <= 10:  # 조건
    result += i  # 처리
    i += 1  # 증가
print('1부터 10까지의 합 :', result)

# while 문을 for로 전환할 수 있어야 함!
result = 0
for i in range(1, 11):
    result += i
print('1부터 10까지의 합 :', result)