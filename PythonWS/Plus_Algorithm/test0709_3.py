# 프로그램 목적: 팩토리얼과 피보나치 수열을 구하는 함수정의
# fibonacci series: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> ..
# 5! = 5 x 4 x 3 x 2 x 1 = 5 x 4! = 5 x 4 x 3! = ...
# 속도는 반복문이 재귀호출보다 훨씬 빠르다
# 드레그 refactor -> method로 하면 코드블럭 생성가능


def fac1(n):  # 반복문을 이용한 팩토리얼 구하기 (iteration)
    k = 1
    for i in range(n, 0, -1):
        k *= i
    return k


def fac2(n):  # 재귀호출을 이용한 팩토리얼 구하기 (recursion)
    if n == 1:  # n == 0으로 해도 상관은 없음
        return 1
    else:
        return n * fac2(n-1)


def fibo(n):  # 재귀호출을 이용하여 피보나치 수열을 구현 (recursion)
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fac1(3))
print(fac2(3))
print(fibo(3))

if __name__ == '__main__':  # 이렇게 해놓으면 해당 파일에 있을 때만 실행가능
    k1 = fac1(5)
    k2 = fac2(5)
    print(k1, k2)