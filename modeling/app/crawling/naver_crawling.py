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
    return live_link

def get_chat_data(html):
    driver.get(html)
    
    bf_program = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text #프로그램이름
    program= re.sub("[?|<|>|?|:]","",bf_program)
    program= re.sub(" ","_",program)

    print(program)
    num = driver.find_elements_by_class_name('LiveHeader_count_1GinT') #영상 header
    play = num[0].text #시청자수
    love = num[1].text #좋아요수
    ids = driver.find_elements_by_class_name("Comment_id_3pR4u") # 채팅 id
    comments = driver.find_elements_by_class_name('Comment_comment_2d0tc') # 채팅 내용

# id와 채팅리스트 text화
    id_list = [id.text for id in ids]
    comment_list = [comment.text for comment in comments]
        
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
    address= "D:\crawling_naver\\data\\0514\\" # 저장경로 지정하기
    file_name = os.path.join(address + f"{program}.csv")
    print("경로+파일",file_name) #어떤 프로그램을 수집하는 지 확인 차 출력
    
# 기존에 존재하는 지 여부 확인
    if os.path.exists(file_name):
        prev_df = pd.read_csv(file_name)
        result = pd.concat([prev_df,df], axis=0)
        
        # ID와 내용 기준으로 중복되는 것 DROP 시키고, 첫번째는 남기는 조건, 인덱스 재정렬
        re_result= result.drop_duplicates(["id","comment"], keep="first", ignore_index= True)
        # 다시 저장하기!
        re_result.to_csv(file_name, index= False)
    else:
        df.to_csv(file_name, index= False)
    return df


# ======================실제 실행되는 부분=====================
# 정해진 시간동안 홈페이지의 10개 방송을 반복하여 데이터 수집 진행되도록
current = datetime.datetime.now()
ten_minutes_later = current + datetime.timedelta(minutes=10) # 10분
half_hours_later= current + datetime.timedelta(minutes=30) # 30분

while True:
    shopping_links = get_home_links(10)
    for i in shopping_links:
        try:
            get_chat_data(i)
        except:
            print("오류발생")
            pass
    currentTime = datetime.datetime.now()
    if (half_hours_later <= currentTime):
        break