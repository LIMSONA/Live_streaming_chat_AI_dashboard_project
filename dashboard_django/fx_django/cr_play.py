from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt
from bs4 import BeautifulSoup
import os
os.environ['WDM_LOG_LEVEL'] = '0' #크롬 시작문구들 안뜨게
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def youtube_play(video_url):
    a=0
    while a==0:   
        try:
            driver.get(url=video_url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            play = driver.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]').text
            play2 =str(play).split()[1]
            print(play2)
        except:
            pass
  

        
def naver_play(video_url):
    a=0
    while a==0:
        try:
            # print("네이버")
            driver.get(url=video_url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            play = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[2]/span[2]').text
            print(play)
        except:
            pass

want= input()
if "youtube" in want:
    youtube_play(want)
else:
    naver_play(want)
