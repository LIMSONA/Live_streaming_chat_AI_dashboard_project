import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt

import cr_kafka # 카프카파일명
import cr_token # 토큰파일명

ck = cr_kafka.c_kafka() # c_kafka 클래스
ct = cr_token.c_token() # c_token 클래스



class c_crawling:   
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

# 1. 유튜브 
# url 예시 https://www.youtube.com/watch?v=py_phbQxy5Y
# 제목클래스 h1 / style-scope ytd-video-primary-info-renderer
    def youtube_kafka(self, video_url, topic_name):
        num= 0
        video_id= video_url.split('?v=')[-1]
        chat = pytchat.create(video_id= video_id)
        ck.init_producer()
        while chat.is_alive():
            try:
                for c in chat.get().sync_items():               
                    # c.datetime 채팅시간 / c.author.name 채팅닉네임 / c.message 채팅내용
                    # 영상unique값 / num / 시간 / 닉네임 / 채팅
                    
                    t_chat_message= ct.preprocessing(c.message)
                    data= self.save_json(video_id, num,
                                         c.datetime, c.author.name,
                                         t_chat_message)#c.message
                    num +=1 #하나씩 커지게
                    ck.pro_kafka(topic_name, data) #카프카로 태우기
                    
            except KeyboardInterrupt: # ctrl + c
                chat.terminate() # 유튜브 긁어오는거 중지
                break
            
# 2. 네이버쇼핑
# url 예시: https://shoppinglive.naver.com/lives/177021
    def naver_kafka(self, video_url, topic_name):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
        options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        video_id = video_url.split("/")[-1]

        num= 0 #while 반복문 상관없이 cnt 되도록
        
        try:
            ck.init_producer()
            driver.get(video_url)
            pop_list = []
            # 영상 제목
            n_title = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
            # print(n_title)
            while True:

                # 채팅 id와 내용
                n_chat_name = driver.find_elements_by_class_name('Comment_id_3pR4u')
                n_chat_message = driver.find_elements_by_class_name('Comment_comment_2d0tc')
                chat_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                
                
                for i in range(len(n_chat_message)):
                    try:
                        if n_chat_name[i].text: #채팅이 있는 경우
                            t_chat_message= ct.preprocessing(n_chat_message[i].text)
                            chat_text = (n_chat_name[i].text, n_chat_message[i].text)
                            if chat_text in pop_list: #중복되는 경우
                                pass
                            else: #중복되지 않는 경우
                                pop_list.append(chat_text)
                                t_chat_message= ct.preprocessing(n_chat_message[i].text)
                                # print(n_chat_message[i].text)
                                # print(t_chat_message)
                                data= self.save_json(video_id, num,
                                                     chat_time, n_chat_name[i].text,
                                                     t_chat_message)
                                num +=1 #하나씩 커지게
                                ck.pro_kafka(topic_name, data) #카프카로 태우기
                    except:
                        pass    
        finally:
            driver.close()