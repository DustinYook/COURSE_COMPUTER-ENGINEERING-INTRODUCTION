# 프로그램 목적: enumerate()는 인덱스를 뽑고, 데이터를 뽑아 튜플을 만듦
# 접근하기 위해서는 print(i[0], i[1])과 같이 쓸 수 있음 -> 인덱스를 뽑기 위해서 사용 (enumerate())

a = [10, 20, 4, 2]
for i, val in enumerate(a):  # enumerate()는 (index, data)로 구성된 튜플을 생성
    print(i, val)  # (0, 10) -> (1, 20) -> (2, 4) -> (3, 2)