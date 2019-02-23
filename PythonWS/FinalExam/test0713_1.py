# 1) 딕셔너리 값 설정하기
d = {}
d['price'] = 100
print(d)

d = dict(price= 100)  # 이거 틀림
print(d)

# 2) 리스트에 값 넣기
l = list()
for i in range(0, 10, 1):
    l.append(i)
l.reverse()
print(l)
# l = list()
# for i in range(9, 0, -1):
#     l.append(i)
# l.reverse()
# print(l)

# 3-1) 정규표현식을 이용하여 추출하기
import re
str = 'width="40" name="KT" height="50"'
extract = re.findall(r'width="([0-9]+)".+?height="([0-9]+)', str)
print(extract)
for width, height in extract:
    print(int(width) + int(height))

# 3-2) 정규표현식을 이용하여 추출하기
import re
str = 'width="40" name="KT" height="50"'
extract = re.findall(r'width="([0-9]+)".+?height="([0-9]+)', str)
width = int(extract[0][0])
height = int(extract[0][1])
print(width + height)