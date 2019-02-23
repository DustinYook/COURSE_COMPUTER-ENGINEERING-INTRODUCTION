# 프로그램 목적: 다른 디렉토리에 정의된 함수 쓰는 방법 1
import Chapter7.test0705_3 as ref  # 이렇게 경로지정 (as는 선택사항)

# <Chapter7/test0705_3.py>
# def prints():  # 함수정의
#     print('123')
#     print('ABC')
#     print('우리나라')
# prints()  # 함수호출
# prints()
# prints()

a = ref.test0705_3.prints()
print(a)