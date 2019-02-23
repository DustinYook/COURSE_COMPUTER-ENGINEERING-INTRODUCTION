# 프로그램 목적: '네이버-증권-국내 증시'에서 Top종목에 대한 정보를 추출하여 'result.csv'에 저장
from urllib import request
import re

# 1. 파일열기
fp = open('result.csv', 'w', encoding='utf-8')

# 2. HTML 문서 가져오기
page = 'https://finance.naver.com/sise/'
content = request.urlopen(page).read()  # HTML 열고, 읽어오기
text = content.decode(encoding='cp949')  # 읽어온 문서를 디코딩
# 참고) 'cp949'로 해야 한글 깨짐현상 방지가능

# 3. 태그에서 데이터 추출하기
# 1) Top 종목에 관한 <div> 태그 추출
top_div_tag = re.findall(r'<div class="box_type_l">.+?<div class="c"></div>', text, re.DOTALL)
for top_div in top_div_tag:
    # 2) <table> 태그 추출
    table_tag = re.findall(r'<table.+?</table>', top_div, re.DOTALL)
    # 3) <caption> 태그 추출
    caption_tag = re.findall(r'<caption>(.+?)</caption>', table_tag[0])
    fp.write('<{}>'.format(caption_tag[0]) + '\n')
    # 4) <th> 태그 추출
    th_tag = re.findall(r'<th>(.+?)</th>', table_tag[0])
    th_tag.insert(5, '전일비')
    for th in th_tag:
        fp.write(th + ' ')
    fp.write('\n')
    # 5) <td> 태그 추출 - 순위
    td_tc_tag = re.findall(r'src="https://ssl.pstatic.net/imgstock/images5/ico_n(.+?).gif', table_tag[0])
    tc_list = list()  # 데이터를 읽어들여 리스트에 저장
    for i in range(0, len(td_tc_tag)):
        tc_list.append(td_tc_tag[i])
    # 6) <td> 태그 추출 - 종목
    a_title_tag = re.findall(r'<a href=".+?</a></td>', table_tag[0])
    title_list = list()  # 데이터를 읽어들여 리스트에 저장
    for a_title in a_title_tag:
        title_list.append(re.findall(r'>(.+?)</a>', a_title))
    # 7) <td> 태그 추출 - 수치 데이터
    td_number_tag = re.findall(r'<td class="number">(.+?)</td>', table_tag[0])
    ceil = len(td_number_tag) // 7
    row_list = list()  # 데이터를 읽어들여 리스트에 저장
    for i in range(ceil):
        row_list.append(td_number_tag[(i * 7):(i + 1) * 7])  # 슬라이싱
    # 8) <span> 태그 추출 - 전일비, 등락률
    span_tah_tag = re.findall(r'<span class="tah p11 red01">(.+?)</span>', table_tag[0], re.DOTALL)
    jib_list = list()
    drr_list = list()
    for num in range(0, len(span_tah_tag)):
        if num % 2 == 0:  # 짝수번째이면 전일비
            jib_list.append(span_tah_tag[num][5:-5])
        else:  # 홀수번째이면 등락률
            drr_list.append(span_tah_tag[num][5:-5])

    # 4. 파일에 출력위해 정렬된 리스트 생성
    data_list = list()
    for num in range(len(td_tc_tag)):
        data_list.insert(0, tc_list[num])  # 순위
        data_list.insert(1, row_list[num][0])  # 연속
        data_list.insert(2, row_list[num][1])  # 누적
        data_list.insert(3, title_list[num][0])  # (종목명)
        data_list.insert(4, row_list[num][2])  # 현재가
        data_list.insert(5, jib_list[num])  # (전일비)
        data_list.insert(6, drr_list[num])  # (등락률)
        data_list.insert(7, row_list[num][3])  # 거래량
        data_list.insert(8, row_list[num][4])  # 시가
        data_list.insert(9, row_list[num][5])  # 고가
        data_list.insert(10, row_list[num][6])  # 저가

    # 5. 정렬된 리스트를 파일에 쓰기처리
    for m in range(len(td_tc_tag)):  #
        for n in range(11*(m-1), 11*m):  # 한 줄 모두 출력 시 줄바꿈 수행
            fp.write(data_list[n] + ' ')
        fp.write('\n')

# 6. 파일에서 읽어오기
fp = open('result.csv', 'r', encoding='utf-8')
print(fp.read())