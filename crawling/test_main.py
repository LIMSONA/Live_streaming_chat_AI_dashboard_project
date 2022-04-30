# 원하는 사이트와 url에서 작업을 하기위해서는 !

from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time
import os
from dotenv import load_dotenv

import re
from konlpy.tag import Okt
from jamo import h2j, j2hcj #초성/중성/종성분리

import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt

import cr_kafka # 카프카 파일명
import cr_token # 토큰 파일명
import cr_crawling # 크롤링 파일명

ck = cr_kafka.c_kafka() # c_kafka 클래스
ct = cr_token.c_token() # c_token 클래스
cr = cr_crawling.c_crawling() # crawling 클래스


# 카프카 
kafka_topic= ['input', 'output']

# 유튜브 크롤링 test
# video_url = "https://www.youtube.com/watch?v=py_phbQxy5Y"

# video_url = str(input())
video_url= "https://www.youtube.com/watch?v=py_phbQxy5Y"
if "youtube" in video_url:
    print("유튜브방송!")
    cr.youtube_kafka(video_url, kafka_topic[0])
else:
    print("네이버방송!")
    cr.naver_kafka(video_url, kafka_topic[0])
    