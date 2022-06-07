import time
# from sqlalchemy import true
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
from threading import Lock, Thread

from . import test_main

import urllib
import glob
import os

from home.crawling import cr_kafka
from home.fx_django import cr_wordcloud

# from cr_kafka import c_kafka
lock = Lock() 
    
options = webdriver.ChromeOptions()
options.add_argument('--headless')

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

already_videos = []

# def youtube_host(video_url):
#     try:
#         driver.get(url=video_url)
#         host = driver.find_element_by_xpath('//*[@id="text"]/a').text
#         print(host)..
#     except:
#         print("오류발생")
        
        
def naver_host(request): 
    try:    
        # 전송된 파라미터(유알엘)을 디코딩함
        url = urllib.parse.unquote(request.GET.get("url")) 
        # 셀레니움에 해당 유알엘로 이동하도록 요청 
        driver.get(url=url) 
        
        type = ""
        videoId = ""
        
        if "shoppinglive.naver.com" in url:
            # naver
            # https://shoppinglive.naver.com/lives/544780?fm=shoppinglive&sn=home
            type = "naver"
            videoId = url.split("/")[-1]
        else :
            # youtube
            # https://www.youtube.com/watch?v=qT4RPpGXlAo
            type = "youtube"
            videoId = url.split("v=")[1]
        
        lock.acquire()
        global already_videos
        if videoId not in already_videos:
            already_videos.append(videoId)
            thread = Thread(target = test_main.startSaveChat, args = (type, url))
            thread.isDaemon = True
            thread.start()
            
            thread = Thread(target = cr_wordcloud.make_wordcloud, args = (url,))
            thread.isDaemon = True
            thread.start()
            
        lock.release()
        
        if type == "naver":
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
        consumer = cr_kafka.con_kafka("input")
        
        #화면에 전달 할 메세지 목록 배열 객체 생성
        chats = []
        
        # videoId = "test"
        # 카프카에서 전달 받은 메세지 목록을 반복함
        for message in consumer:
            # 해당 메세지의 비디오를 식별함 (예시는 유튜브의 영상 아이디)
            if(message.value["video_unique"] == videoId): 
                # 메세지 목록 배열에 메세지 내용 추가
                chats.append(message.value)
        
        files = glob.glob("mysite/static/image/*.png")
        if len(files) > 0:
            wordcloudImg = max(files, key=os.path.getctime)
        else:
            wordcloudImg = ""
        
        # 화면에 전달 할 객체 생성
        data = {
            "host" : host,
            "love" : love,
            "play" : play,
            "program" : program,
            "chats" : chats,
            "image" : wordcloudImg
        }
        
        # 위에서 생성한 객체를 제이슨 객체로 페이지에 반환
        return JsonResponse(data)
    except:
        return HttpResponse("error");





