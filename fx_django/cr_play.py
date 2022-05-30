from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt
from bs4 import BeautifulSoup 

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def youtube_play(video_url):
    try:
        while True :
            driver.get(url=video_url)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            play = driver.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]').text
            play2 =str(play).split()[1]
            return play2
    except:
        return "오류발생"
    finally:
            driver.close()    

        
def naver_play(video_url):
    try:
        while True:
            driver.get(video_url)
            # 영상 제목
            n_title = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
            return n_title
    except:
        return "오류발생"
    finally:
            driver.close()

want= input()
if "youtube" in want:
    youtube_play(want)
else:
    naver_play(want)
