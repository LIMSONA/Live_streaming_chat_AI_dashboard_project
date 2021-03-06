# 원하는 사이트와 url에서 작업을 하기위해서는 !

from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time
import os

import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt

from home.crawling import cr_kafka # 카프카 파일명
from home.crawling import cr_token # 토큰 파일명 
from home.crawling import cr_crawling # 크롤링 파일명 

ck = cr_kafka.c_kafka() # c_kafka 클래스
ct = cr_token.c_token() # c_token 클래스
cr = cr_crawling.c_crawling() # crawling 클래스 


# 카프카 
kafka_topic= ['input']  

# 유튜브 크롤링 test

def startSaveChat(want, video_url):
    if "youtube" in video_url:
        print("youtube streaming!")
        cr.youtube_kafka(video_url, kafka_topic[0])
    else:
        print("naver  streaming!")
        cr.naver_kafka(video_url, kafka_topic[0])
        
