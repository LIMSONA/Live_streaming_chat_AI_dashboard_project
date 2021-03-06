from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import pytchat
import time
import datetime 
import pandas as pdSS
import os
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
okt= Okt()    
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def crawling_5(want):
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
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        while True:
            driver.get(want)
            pop_list= []
            # 채팅 id와 내용
            n_chat_message = driver.find_elements_by_class_name('Comment_comment_2d0tc')
            
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
            
def crawling_30(want):
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
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        while True:
            driver.get(want)
            pop_list= []
            # 채팅 id와 내용
            n_chat_message = driver.find_elements_by_class_name('Comment_comment_2d0tc')
            
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
def word_cloud(bucket):
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
        mask= np.array(Image.open('C:\git\\hy22-platform\\fx_django\\youtube_1.png'))
        image_colors = ImageColorGenerator(mask)
        # #유튜브 mask 2
        # mask= np.array(Image.open('C:\git\\hy22-platform\\fx_django\\youtube_2.png'))
        # image_colors = ImageColorGenerator(mask)
    else:
        #네이버
        mask= np.array(Image.open('C:\git\\hy22-platform\\fx_django\\naver.png'))
        image_colors = ImageColorGenerator(mask)

        
    font = 'C:\git\\hy22-platform\\fx_django\\BMHANNA_11yrs_ttf.ttf'
    # mask = np.array(Image.open('C:\git\\hy22-platform\\fx_django\\comments.png'))
    wc= WordCloud(font_path=font, width=400, height=400, 
                scale=2.0, max_font_size=250, background_color="white", mask=mask)
    gen=wc.generate_from_frequencies(counts)
    # gen= wc.recolor(color_func=image_colors)
    
    # plt.figure()
    # plt.imshow(gen)
    # 파일명은 날짜와 시간형식으로  
    time= datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    # plt.savefig('c_wordcloud_{time}.png')
    gen.to_file("C:\git\\hy22-platform\\fx_django\\image\\imagewordcloud_{}.png".format(time))

# url 받고
want= input()
# want= "https://shoppinglive.naver.com/lives/541905?fm=shoppinglive&sn=home"
#현재시간으로 부터 +30초 이전
#5초동안 크롤링 => 워드클라우드  ---->  총6번
for i in range(6):
    bucket=[]
    crawling_5(want)
    # print("워드클라우드 여기======================================")
    # print(bucket)
    word_cloud(bucket)


#현재시간으로부터 +30초 이후인가?
#30초이후 오류생기지 않는 한 반복 
#30초동안 크롤링 => 워드클라우드
while True:
    bucket=[]
    crawling_30(want)
    # print("워드클라우드 여기=================================")
    word_cloud(bucket)
    
    
