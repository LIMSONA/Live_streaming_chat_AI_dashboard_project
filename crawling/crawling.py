import pytchat
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from datetime import datetime as dt

import cr_kafka.c_kafka #파일명.클래스



class crawling:
    
# 유튜브 
# url 예시 https://www.youtube.com/watch?v=py_phbQxy5Y
    def youtube_kafka(self, video_url, topic_name):
        video_id= video_url.split('?v=')[-1]
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                data=f"{c.message}"
                print(data)  # 채팅내용
                

#네이버쇼핑
# url 예시: https://shoppinglive.naver.com/lives/177021
    def naver_kafka(self,)
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
        n_chat_comment = driver.find_elements_by_class_name('Comment_comment_2d0tc')
        # c_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        
        
        for i in range(len(n_chat_comment)):
            
            try:
                if n_chat_id[i].text:
                    chat_text = (n_chat_id[i].text, n_chat_comment[i].text)
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
