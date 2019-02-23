# 프로그램 목적: 웹툰리스트와 썸네일 이미지를 특정폴더에 저장
import requests  # 'urllib'의 향상된 버전
import re  # 정규표현식을 사용하기 위함
import os   # 디렉토리 없는 경우 처리하기 위함

url = 'https://comic.naver.com/webtoon/weekday.nhn'
received_data = requests.get(url)  # 참고) 기존엔 request.urlopen(url).read() 사용
txt = received_data.text  # 참고) 기존엔 received_data.decode('utf-8') 사용
week = re.findall(r'<div class="col_inner">.+?</ul>', txt, re.DOTALL)

dayList = list()
names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
for index, day in enumerate(week):  # enumerate()는 인덱스를 붙여 튜플생성
    # 이렇게 하면 튜플로 들어감 -> 인덱스는 요일 (0: 월요일, 1: 화요일, ..)
    li = re.findall(r'<li>.+?</li>', day, re.DOTALL)
    for item in li:  # 주의) 잡다한 것은 '.+?', 소괄호는 뽑아오는 대상
        info = re.findall(r'src="(.+?)".+?title="(.+?)"', item, re.DOTALL)  # 여기서 소괄호 2개 뽑아옴 -> 튜플
        for image, title in info:
            if not'.gif' in image:  # 'image'에서 '.gif' 제거
                dayList.append((names[index], image, title))  # names[index]를 통해 문자상수구현
                # print(*dayList, sep='\n')  # 여기에 *를 넣어야 함

if not os.path.exists('Image'):  # 디렉토리가 없는 경우 처리
    os.mkdir('Image')  # 'Image'라는 디렉토리 생성


def save_image(d, i, t):
    title = re.sub(r'\?', '', t)  # re.sub(r'제거패턴', '대체패턴', 대상)
    # 중요) format()을 통해서 파일경로/파일명도 생성가능
    filename = 'Image/{}.{}'.format(title, 'jpg')
    received_image = requests.get(i)  # 'i'는 이미지 경로
    fp = open(filename, 'wb')  # 'wb'는 바이너리로 파일작성 (이미지에 사용)
    fp.write(received_image.content)
    fp.close()  # 파일닫기


for day, image, title in dayList:
    save_image(day, image, title)