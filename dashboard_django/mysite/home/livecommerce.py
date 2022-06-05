
import time
from kafka import KafkaProducer, KafkaConsumer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django.http import HttpResponse, JsonResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from json import loads

from json import dumps
import random
from kafka.admin import KafkaAdminClient, NewTopic

import startbutton

import urllib
# from cr_kafka import c_kafka
#
options = webdriver.ChromeOptions()
options.add_argument('--headless')

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# def youtube_host(video_url):
#     try:
#         driver.get(url=video_url)
#         host = driver.find_element_by_xpath('//*[@id="text"]/a').text
#         print(host)
#     except:
#         print("오류발생")
        
        
def naver_host(request): 
    # try:
    
    # 전송된 파라미터(유알엘)을 디코딩함
    url = urllib.parse.unquote(request.GET.get("url")) 
    # 셀레니움에 해당 유알엘로 이동하도록 요청 
    driver.get(url=url) 
    
    type = ""
    videoId = ""
    
    if "shoppinglive.naver.com" in url:
        # naver
        # https://shoppinglive.naver.com/lives/544780?fm=shoppinglive&sn=home
        type = "N"
        videoId = url.split("/")[4]
        if "?" in videoId:
            videoId = videoId.split("?")[0]
    else :
        # youtube
        # https://www.youtube.com/watch?v=qT4RPpGXlAo
        type = "Y"
        videoId = url.split("v=")[1]
        
    
    if type == "N":
        # 로드 된 셀레니움 객체 내에서 호스트 명이 들어있는 엘리먼트를 찾음
        host = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[1]').text
        
        # 좋아요 갯수 엘리먼트는 최초 로드 시 없을 수 있기때문에 최대 10초까지 해당 엘리먼트의 노출을 기다림
        loveElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/div/span[3]/span[2]'))
        )
        love = loveElement.text
        
        # 재생횟수 갯수 엘리먼트는 최초 로드 시 없을 수 있기때문에 최대 10초까지 해당 엘리먼트의 노출을 기다림
        playElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/div/span[2]/span[2]'))
        )
        play = playElement.text
        
        # 프로그램 엘리먼트를 찾아 옴
        program = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/h2').text
    else :
        # youtube parse logic in here 
        hostElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#text-container > yt-formatted-string > a'))
        )
        host = hostElement.text
         
        loveElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#top-level-buttons-computed > ytd-toggle-button-renderer:nth-child(1) > a > yt-formatted-string'))
        )
        love = loveElement.text
        
        playElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#count > ytd-video-view-count-renderer > span.view-count.style-scope.ytd-video-view-count-renderer'))
        )
        play = playElement.text
        
        program = driver.find_element_by_css_selector('#container > h1 > yt-formatted-string').text
        
    # 카프카에 해당 토픽명에 해당하는 항목을 요청함
    consumer = con_kafka("message")
    
    #화면에 전달 할 메세지 목록 배열 객체 생성
    chats = []
    
    # videoId = "test"
    # 카프카에서 전달 받은 메세지 목록을 반복함
    for message in consumer:
        # 해당 메세지의 비디오를 식별함 (예시는 유튜브의 영상 아이디)
        if(message.value["video_unique"] == videoId): 
            # 메세지 목록 배열에 메세지 내용 추가
            chats.append(message.value)
    
    # 화면에 전달 할 객체 생성
    data = {
        "host" : host,
        "love" : love,
        "play" : play,
        "program" : program,
        "chats" : chats
    }
    
    # 위에서 생성한 객체를 제이슨 객체로 페이지에 반환
    return JsonResponse(data)
    # except:
    #     return HttpResponse("error");





bootstrap_servers="kafka:9092"
def con_kafka(topic_name):      
    consumer = KafkaConsumer(
                topic_name,
                bootstrap_servers=[bootstrap_servers],
                auto_offset_reset='earliest', # 또는 latest
                enable_auto_commit=True,
                group_id=None, #일단 그룹아이디 만들지 말고
                value_deserializer=lambda x: loads(x.decode('utf-8')),
                consumer_timeout_ms=1000
                )
    return consumer    


# topic_name = "message" #토픽확인! 
# producer = KafkaProducer(
#         acks=0,
#         compression_type='gzip',
#         bootstrap_servers=[bootstrap_servers],
#         value_serializer=lambda x: dumps(x).encode('utf-8')
#         )


# print("[begin] producer가 메세지전송 시작")

# # video_unique	num	chat_time	chat_id	chat_message	swear_score	pn_score	qa_score
# # 실시간 방송 이름	1	시스템 시간	작성자 닉네임	채팅내용	1	1	0

# #10000개 갖고 오기

# for i in range(100):
#     swear = random.randrange(0,2)
#     pn = random.randrange(0,2)
#     qa = random.randrange(0,2)
    
#     data = {'video_unique':"-JhoMGoAfFc"
#             ,'num':i
#             ,'chat_time': time.time()
#             ,'chat_id':"user_" + str(i) 
#             ,'chat_message': ("정상" if swear == 0 else "욕설") 
#                             +("긍정" if pn == 0 else "부정") 
#                             +("질문" if qa == 1 else "일반") 
#                                 + str(i)
#             ,'swear_score':swear
#             ,'pn_score':pn
#             ,'qa_score':qa
# }
#     print("메세지 전송중 ...")
#     producer.send(topic_name, value=data)
#     producer.flush()





