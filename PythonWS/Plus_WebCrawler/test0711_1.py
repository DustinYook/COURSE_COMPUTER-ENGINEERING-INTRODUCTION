# 프로그램 목적: 크롤링과 파일처리 기초실습
# 요약: 웹크롤링 -> 화면출력/파일쓰기 -> 파일읽기
from urllib import request, parse
import re

# 1) 파일열기
fp = open('data.csv', 'w', encoding='utf-8')  # csv 확장자는 콤마(,)로 구분된 데이터 저장 시 주로 이용
# open('읽을 파일', '모드', encoding='인코딩')

# 2) HTML 문서 받아오기
# 1단계: 받아올 URL 설정
page = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
# 2단계: 'urllib.request'에 정의된 urlopen()을 통해 열고, read()를 통해 읽어옴
content = request.urlopen(page).read()  # <=> request.urlopen() -> content.read()
# 3단계: UTF-8 형식을 갖추어 디코딩
text = content.decode('utf-8')

# 3) 쿼리 스트링 처리
num = int(input('지역번호를 입력해주십시오 : '))
area = {'stnId': num}  # 딕셔너리에 저장
query_string = parse.urlencode(area)  # 'urllib.parse'에서 urlencode() 통해 쿼리 스트링으로 변환
page = page + '?' + query_string  # 연결연산을 통해 URL과 연결시킴

# 4) 정규표현식을 통해 데이터 추출
location_tag = re.findall(r'<location wl_ver="3">.+?</location>', text, re.DOTALL)
# 줄바꿈 무시: re.DOTALL -> 한 줄로 구성된 데이터는 굳이 이를 사용할 필요가 없다
for location in location_tag:
    province = re.findall(r'<province>(.+)</province>', location)  # 하위식 추출에는 소괄호 이용
    city = re.findall(r'<city>(.+)</city>', location)

    # data_tag = re.findall(r'<data>.+?</data>', text, re.DOTALL)  # 이슈: 대상이 'text'로 범위가 너무 넓음
    data_tag = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)  # 해결: 범위를 'location'으로 좁힘
    # print(len(data_tag), data_tag)  # 13 ['\r\n\t\t\t\t\t...', '\r\n\t\t\t\t\t...', ...]
    # '.+?'는 <data> </data>를 한 덩어리로 인식하여 끊어 줌, 위에서는 그렇게 끊은 것이 13 덩어리라는 의미
    # 중간에 임의의 것(.)이 한 번 이상(+) 나올 수 있으므로 (.+)을 쓰는 것이다
    # data_tag = re.findall(r'<data>(.+)</data>', location, re.DOTALL)  # '.+'는 한 덩어리로 인지
    # print(len(data_tag), data_tag)  # 1 ['\r\n\t\t\t\t\t<mode>A02</mode>\r\n\t\t\t\t\t...']

    # 5) 파일에 쓰기 처리
    result1 = '{} | {} '.format(province[0], city[0])
    fp.write(result1 + '\n')  # 파일에 쓰기 처리
    for data in data_tag:
        # print(len(data))  # len()을 사용하면 정규표현식으로 받아온 요소의 개수를 알 수 있다
        mode = re.findall(r'<mode>(.+)</mode>', data)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', data)
        wf = re.findall(r'<wf>(.+)</wf>', data)
        tmn = re.findall(r'<tmn>(.+)</tmn>', data)
        tmx = re.findall(r'<tmx>(.+)</tmx>', data)
        reliability = re.findall(r'<reliability>(.+)</reliability>', data)
        result2 = '{} | {} | {} | {} | {} | {}'.format(mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reliability[0])
        # format()은 인자를 받아 형식에 맞게 문자열을 생성하는 함수이다
        fp.write(result2 + '\n')  # 개행문자 지정해야 제대로 출력
    fp.write('\n')

# 6) 파일을 읽어 화면에 출력
fp = open('data.csv', 'r', encoding='utf-8')  # r: read 모드
print('\n' + fp.read())  # fp.read()는 파일을 읽어옴