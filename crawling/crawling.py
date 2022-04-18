import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from datetime import datetime as dt

import cr_kafka # 카프카파일명
import cr_token # 토큰파일명

ck = cr_kafka.c_kafka # c_kafka 클래스
ct = cr_token.c_token # c_token 클래스


class crawling:
    
# 0. json형식 파일저장하기
# 영상unique값 / 시간 / 닉네임 / 채팅 / 명사 토큰값 
    def save_json(self, video_unique, chat_time, chat_name, chat_message):
        json_form= {
        "video_unique" : video_unique,
        "chat_time" : chat_time,
        "chat_id" : chat_name,
        "Chat_message" : chat_message,
        "chat_n_token" : ct.noun_tokenize(chat_message)}
        return json_form
    
# 1. 유튜브 
# url 예시 https://www.youtube.com/watch?v=py_phbQxy5Y
# 제목클래스 h1 / style-scope ytd-video-primary-info-renderer

    def youtube_kafka(self, video_url, topic_name):
        video_id= video_url.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                data=f"{c.message}"
                print(data)  # 채팅내용                
                # c.datetime 채팅시간 / c.author.name 채팅닉네임 / c.message 채팅내용

        
         
                
                

# 2. 네이버쇼핑
# url 예시: https://shoppinglive.naver.com/lives/177021
    def naver_kafka(self,url_val, topic_name):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        url_val = "https://shoppinglive.naver.com/lives/487251"
        # url_id = url_val.split("/")[-1]


        old_poplist = []
        try:
            
            while True:
                driver.get(url_val)
                pop_list = []
                
                #채팅 제목
                n_liveheader = driver.find_element_by_class_name('LiveHeader_text_2XGaZ')
                n_title = n_liveheader.text
                print(n_title)

                # 채팅 id와 내용
                n_chat_id = driver.find_elements_by_class_name('Comment_id_3pR4u')
                n_chat_message = driver.find_elements_by_class_name('Comment_comment_2d0tc')
                # c_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                
                
                for i in range(len(n_chat_message)):
                    
                    try:
                        if n_chat_id[i].text:
                            chat_text = (n_chat_id[i].text, n_chat_message[i].text)
                            if chat_text in pop_list:
                                pass
                            else:
                                pop_list.append(chat_text)
                            
                    except:
                        pass

                for i in pop_list:
                    print(i)
                print("=========================================================================================")
                time.sleep(5)
            
        finally:
            driver.close()
