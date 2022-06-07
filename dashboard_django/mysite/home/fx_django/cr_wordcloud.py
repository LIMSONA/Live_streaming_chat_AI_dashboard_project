from konlpy.tag import Okt
from collections import Counter

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import pytchat
import time
import datetime 
import os
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import os

from home.crawling.cr_kafka import c_kafka

okt= Okt()    

currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"

def crawling_5(bucket, want):
    current= datetime.datetime.now()
    
    
# 유튜브
    if "youtube" in want:
        print("유튜브")
        video_id= want.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
        while True:
            for c in chat.get().sync_items():
                re_string= re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+',"", str(c.message))
                bucket.append(re_string) #워드클라우드를 위한 리스트 추가
                print(re_string)
            if datetime.datetime.now() <= current + datetime.timedelta(seconds=5):
                break            
            
# 네이버
    else:
        # print("네이버========================================")
        씨케이 = c_kafka()
        
        consumer = 씨케이.con_kafka("input")
        video_id = want.split("/")[-1]
        
        for message in consumer:
            if video_id in message.value["video_unique"]:
                n_chat_message = message.value["chat_message"]
                
                for i in range(len(n_chat_message)):
                    # if n_chat_message[i].text: #채팅이 있는 경우
                    try:
                        if (n_chat_message[i].text) in pop_list: 
                            pass
                        else: #중복되지 않는 경우
                            pop_list.append(n_chat_message[i].text) #중복을 대조하기 위한 리스트에 추가
                            re_string= re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+',"", str(n_chat_message[i].text)) #워드클라우드를 위한 리스트추가
                            bucket.append(re_string)
                            print(n_chat_message[i].text)
                    except:
                        pass
                if datetime.datetime.now() >= current + datetime.timedelta(seconds=5):
                    break
            
def crawling_30(bucket, want):
    current= datetime.datetime.now()
# 유튜브
    if "youtube" in want:
        print("유튜브")
        video_id= want.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
        while True:
            for c in chat.get().sync_items():
                re_string= re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+',"", str(c.message))
                bucket.append(re_string) #워드클라우드를 위한 리스트 추가
                print(re_string)
            if datetime.datetime.now() <= current + datetime.timedelta(seconds=30):
                break            
            
# 네이버
    else:
        # print("네이버========================================")
        
        씨케이 = c_kafka()
        
        consumer = 씨케이.con_kafka("input")
        video_id = want.split("/")[-1]
        
        for message in consumer:
            if video_id in message.value["video_unique"]:
                n_chat_message = message.value["chat_message"]
                    
                pop_list= []
                for i in range(len(n_chat_message)):
                    # if n_chat_message[i].text: #채팅이 있는 경우
                    try:
                        if (n_chat_message[i].text) in pop_list: 
                            pass
                        else: #중복되지 않는 경우
                            pop_list.append(n_chat_message[i].text) #중복을 대조하기 위한 리스트에 추가
                            re_string= re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+',"", str(n_chat_message[i].text)) #워드클라우드를 위한 리스트추가
                            bucket.append(re_string)
                            print(n_chat_message[i].text)
                    except:
                        pass
                if datetime.datetime.now() >= current + datetime.timedelta(seconds=30):
                    break
 
 
# 워드클라우드 실행
def word_cloud(bucket, want):
    bucket2=[]
    for i in bucket:
        morph= okt.nouns(i)
        # print(morph)
        for j in morph:
            # print(j)
            bucket2.append(j)
    # print(bucket2)
    counts= Counter(bucket2)
    # print(counts)
    
    if "youtube" in want:
        #유튜브 mask 1
        mask= np.array(Image.open(currentPath + 'youtube_1.png'))
        # image_colors = ImageColorGenerator(mask)
        # #유튜브 mask 2
        # mask= np.array(Image.open('C:\git\\hy22-platform\\fx_django\\youtube_2.png'))
        # image_colors = ImageColorGenerator(mask)
    else:
        #네이버
        mask= np.array(Image.open(currentPath + 'naver.png'))
        # image_colors = ImageColorGenerator(mask)

        
    if len(bucket2) > 0:
        font = currentPath + 'BMHANNA_11yrs_ttf.ttf'
        # mask = np.array(Image.open('C:\git\\hy22-platform\\fx_django\\comments.png'))
        wc= WordCloud(font_path=font, width=400, height=400, 
                    scale=2.0, max_font_size=250, background_color="white")
        
        gen=wc.generate_from_frequencies(counts)
        # gen= wc.recolor(color_func=image_colors)
        
        # 파일명은 날짜와 시간형식으로  
        time= datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        gen.to_file("mysite/static/image/wordcloud_{}.png".format(time))

def make_wordcloud(want):
    # url 받고
    # want= input()
    # want= "https://shoppinglive.naver.com/lives/541905?fm=shoppinglive&sn=home"
    #현재시간으로 부터 +30초 이전
    #5초동안 크롤링 => 워드클라우드  ---->  총6번
    for i in range(6):
        bucket=[]
        crawling_5(bucket, want)
        # print("워드클라우드 여기======================================")
        # print(bucket)
        word_cloud(bucket, want)


    #현재시간으로부터 +30초 이후인가?
    #30초이후 오류생기지 않는 한 반복 
    #30초동안 크롤링 => 워드클라우드
    while True:
        bucket=[]
        crawling_30(bucket, want)
        # print("워드클라우드 여기=================================")
        word_cloud(bucket, want)
        
    
