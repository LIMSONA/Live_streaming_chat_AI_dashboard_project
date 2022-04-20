# 크롤링과 토큰화 조합부터 테스트
# 유튜브부터 

import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt

# import cr_kafka # 카프카파일명
import cr_token # 토큰파일명

# ck = cr_kafka.c_kafka() # c_kafka 클래스
ct = cr_token.c_token() # c_token 클래스

class c_crawling:   
# 0. json형식 파일저장하기
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
    def youtube_kafka(self, video_url):
        num= 0
        video_id= video_url.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
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
                    return data
                
            # except KeyboardInterrupt: # ctrl + c
            #     chat.terminate() # 유튜브 긁어오는거 중지
            #     break
            except:
                print("오류 발생의 경우")
                continue



c = c_crawling()
# c.youtube_kafka("https://www.youtube.com/watch?v=py_phbQxy5Y")
result = c.youtube_kafka("https://www.youtube.com/watch?v=py_phbQxy5Y")
import cr_kafka # 카프카파일명
ck= cr_kafka.c_kafka()

ck.pro_kafka("test_topic", result)