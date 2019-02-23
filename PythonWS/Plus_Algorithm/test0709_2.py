# 프로그램 목적: 기본적인 알고리즘 구현
import random


def print_list(arg):
    i = 0
    cnt = 0
    for i in arg:
        print(i, end='\t')
        cnt += 1
        if cnt % 5 == 0:  # 카운트가 5되면 줄바꿈
            print(' ')


# 1~9까지의 숫자 중에서 임의로 20개의 숫자 추출
li = list()
for i in range(20):
    random_num = random.randrange(1, 10)
    li.append(random_num)
print_list(li)


