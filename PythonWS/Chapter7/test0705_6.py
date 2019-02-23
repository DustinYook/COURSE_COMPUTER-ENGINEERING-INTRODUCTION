# 프로그램 목적: 파이썬 함수의 특징 -> 리턴값이 여러개

# 1) 1개 인자를 받아 2개를 리턴
def prints(param):
    result = 10 + param
    return result, param  # 파이썬에서는 리턴값이 2개일 수 있다

print(prints(1))  # 결과값: (11, 1)
r, arg = prints(2)
print(r, arg)  # 결과값: 12 2


# 2) 2개 인자를 받아 2개를 리턴
def prints(param1, param2):
    result1 = param1 + param2
    result2 = param1 - param2
    return result1, result2

print(prints(10, 20))  # 결과값: (30, -10)
r1, r2 = prints(10, 20)
print(r1, r2)  # 결과값: 30 -10