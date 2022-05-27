# # 0. 맨처음
# #--> 맨처음 시간을 변수로 지정해놓고 처음 30초동안엔 5초단위로 쪼개서 워드클라우드
# # 1. 30초동안 작동된다
# # 2. 코멘트를 입력한다. 
# #--> df으로 모아놨다가 한번에 빡 리스트화 시키는 방법
# #--> 코멘트마다 리스트에 추가하는 방법
# # 3. 명사형으로 변환한다.
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
import pytchat
import time
from datetime import datetime, timedelta
import pandas as pd
import os
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from crawling.cr_wordcloud import c_wordcloud


# 처음시작시간 찍고
current = datetime.datetime.now()
thirty_seconds_later = current + datetime.timedelta(seconds=30)




okt= Okt()    
bucket=[]
def crawling(want):
# 유튜브
    if "youtube" in want:
        print("유튜브")
        video_id= want.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                re_string= re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+',"", str(c.message))
                bucket.append(re_string) #워드클라우드를 위한 리스트 추가
# 네이버
    else:
        print("네이버")
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
            # n_chat_name = driver.find_elements_by_class_name('Comment_id_3pR4u')
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



# 워드클라우드 실행
# url 받고
want= input()
# 채팅 크롤링 시행하고
crawling(want)

bucket2=[]
for i in bucket:
    morph= okt.nouns(i)
    for j in morph:
        bucket2.append(j)
    counts= Counter(bucket2)
    mask = np.array(Image.open('comments.png'))
    wc= WordCloud(font_path='C:/Windows/Fonts/BMHANNA_11yrs_ttf.ttf', width=400, height=400, 
                  scale=2.0, max_font_size=250, background_color="white", mask=mask)
    gen= wc.generate_from_frequencies(counts)
    # plt.figure()
    # plt.imshow(gen)
    # 파일명은 날짜와 시간형식으로  
    time= datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    # plt.savefig('c_wordcloud_{time}.png')
    gen.to_file("./imagewordcloud_{}.png".format(time))







# # ★ if <=현재시간이 30초 이전 시점
# currentTime = datetime.datetime.now()
# if currentTime<=thirty_seconds_later:
#     for i in range(5):
        
#         c_wordcloud()        
    
# else:
    
