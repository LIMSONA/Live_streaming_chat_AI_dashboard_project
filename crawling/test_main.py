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
import crawling # 크롤링 파일명

ck = cr_kafka.c_kafka() # c_kafka 클래스
ct = cr_token.c_token() # c_token 클래스
cr = crawling.crawling() # crawling 클래스


# 카프카 
kafka_topic= ['input', 'output']

# 유튜브 크롤링 test
video_url = "https://www.youtube.com/watch?v=py_phbQxy5Y"

class crawling:   
# 0. json형식 파일저장하기
# 영상unique값 / num / 시간 / 닉네임 / 채팅
    def save_json(self, video_unique, num, chat_time, chat_name, chat_message):
        json_form= {
        "video_unique" : video_unique,
        "num" : num,
        "chat_time" : chat_time,
        "chat_id" : chat_name,
        "chat_message" : chat_message}
        # "chat_n_token" : ct.noun_tokenize(chat_message)}
        return json_form

    def youtube_kafka(self, video_url, topic_name):
        num= 0
        video_id= video_url.split('?v=')[-1]
        chat = pytchat.create(video_id= video_id)
        while chat.is_alive():
            try:
                for c in chat.get().sync_items():               
                    # c.datetime 채팅시간 / c.author.name 채팅닉네임 / c.message 채팅내용
                    # 영상unique값 / num / 시간 / 닉네임 / 채팅
                    
                    t_chat_message= ct.preprocessing(c.message)
                    data= self.save_json(video_id, num,
                                            c.datetime, c.author.name,
                                            t_chat_message)
                    num +=1 #하나씩 커지게
                    ck.pro_kafka(topic_name, data) #카프카로 태우기
                    
            except KeyboardInterrupt: # ctrl + c
                chat.terminate() # 유튜브 긁어오는거 중지
                break 
        
        
#테스트 해보기
c= crawling()
c.youtube_kafka(video_url,
                "input")