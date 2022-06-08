from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
from time import sleep
import re
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import os

# 드라이브 실행
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('user-Agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)

# 크롤링할 링크 수집
home_url = "https://shoppinglive.naver.com/home"
driver.get(url= home_url)
homepage_tab = driver.window_handles[0]
sleep(5)

# 홈페이지 링크들 가져오기
def get_home_links(num = 10):
    driver.switch_to.window(homepage_tab)
    driver.get(url= home_url)
    sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    live_panels = soup.find_all("a", class_ = "VideoCard_link_3x4f-")
    live_link = [f"https://shoppinglive.naver.com{panel['href']}" for panel in live_panels]
    live_name = [panel.find("span", class_="VideoCard_title_1Sgl6").text for panel in live_panels]
    live_link = live_link[:num]
#     print(live_name)
    return live_link



# df로 저장하기
def get_chat_data(html):
    driver.get(html)
#     soup = BeautifulSoup(html, "html.parser")
    
    bf_program = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text #프로그램이름
    program= re.sub("[?|<|>|?|:]","",bf_program)
    program= re.sub(" ","_",program)
#     p = re.compile("[?|<|>|?|:]")
#     program= p.sub("", bf_program)
    print(program)
    num = driver.find_elements_by_class_name('LiveHeader_count_1GinT') #영상 header
    play = num[0].text #시청자수
#     print(play)
    love = num[1].text #좋아요수
#     print(love)
    ids = driver.find_elements_by_class_name("Comment_id_3pR4u") # 채팅 id
    comments = driver.find_elements_by_class_name('Comment_comment_2d0tc') # 채팅 내용

# id와 채팅리스트 text화
    id_list = [id.text for id in ids]
    comment_list = [comment.text for comment in comments]

#     print(id_list)
#     print(comment_list)
        
# df 만들기
    df = pd.DataFrame()
    df["id"] = id_list[:30]
    df["comment"] = comment_list[:30]
    df["program"] = program
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") #ex) '2022-04-24_02:19:32'
    df["time"] = time
    df["love"] = love
    df["play"] = play

# 위치+파일명 변수 들어주기
    address= "C:\crawling\\0530_2\\"
    file_name = os.path.join(address + f"{program}.csv")
#     print("경로+파일",file_name)
# 기존에 존재하는 지 여부 확인
    if os.path.exists(file_name):
        prev_df = pd.read_csv(file_name)
#         print(prev_df)
        result = pd.concat([prev_df,df], axis=0)
# ID와 내용 기준으로 중복되는 것 DROP 시키고, 첫번째는 남기는 조건, 인덱스 재정렬
        re_result= result.drop_duplicates(["id","comment"], keep="first", ignore_index= True)
# 다시 저장하기!
        re_result.to_csv(file_name, index= False)   
    else:
#         print(df)
        df.to_csv(file_name, index= False)
    return df

current = datetime.datetime.now()
ten_minutes_later = current + datetime.timedelta(minutes=120)

# 10분동안 반복문 진행되도록!!
while True:
    shopping_links = get_home_links(10)
    for i in shopping_links:
        try:
            get_chat_data(i)
        except:
            print("오류발생")
            pass
#     time.sleep(10)
    currentTime = datetime.datetime.now()
    if (ten_minutes_later <= currentTime):
        break