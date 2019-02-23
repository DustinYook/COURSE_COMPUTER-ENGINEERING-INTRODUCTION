# 프로그램 목적: 다른 디렉토리에 정의된 함수 쓰는 방법 2

# <Chapter7/test0705_3.py>
# def prints():  # 함수정의
#     print('123')
#     print('ABC')
#     print('우리나라')
# prints()  # 함수호출
# prints()
# prints()

import sys   # 이는 test0712_4와 동일
sys.path.insert(0, '../Chapter7/')  # ..는 상위폴더
# 1단계: ..를 통해 올라가서 (python_WorkSpace)
# 2단계: Chapter7으로 이동

import test0705_3
a = test0705_3.prints()
print(a)