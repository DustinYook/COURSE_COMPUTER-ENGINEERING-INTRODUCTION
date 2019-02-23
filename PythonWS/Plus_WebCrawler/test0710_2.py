# 프로그램 목적: 웹 사이트 크롤링 기초실습
from urllib import request, parse

page = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'  # 읽을 페이지 URL 설정
content = request.urlopen(page).read()  # 해당 URL의 HTML 문서를 읽어들임

# 쿼리 스트링에 대한 처리
# 쿼리 스트링이란? 사용자가 입력한 데이터를 서버로 전달하는 가장 단순한 방법
# ex) '?stnId=108'와 같이 나타난 문자열
num = int(input('지역번호를 입력해주십시오: '))
area = {'stnId': num}  # 쿼리 스트링 형식을 가진 딕셔너리를 선언
params = parse.urlencode(area)  # 쿼리 스트링 형태로 인코딩 작업
# parse.urlencode()는 딕셔너리 또는 튜플을 쿼리 스트링으로 만들어 줌
page = page + '?' + params  # 연결연산을 통해 쿼리 스트링 완성
print(content.decode('utf-8'))  # UTF-8 형식을 갖추어 해석