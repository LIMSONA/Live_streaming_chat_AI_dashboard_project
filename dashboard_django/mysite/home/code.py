#host
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup #네이버
#play
from datetime import datetime as dt
import requests
########

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


################# host #######################
# def youtube_host(video_url):
#     try:
#         driver.get(url=video_url)
#         html = driver.page_source
#         soup = BeautifulSoup(html, "html.parser")
#         host = driver.find_element_by_xpath('//*[@id="text"]/a').text
#         print(host)
#     except:
#         print("오류발생")
         
def naver_host(video_url):   
    try:
        driver.get(url=video_url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        host = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[1]').text
        print(host)
    except:
        print("오류발생")

# want= input()
# if "youtube" in want:
#     youtube_host(want)
# else:
#     naver_host(want)


################# play #######################
# def youtube_play(video_url):
#     a=0
#     while a==0:   
#         try:
#             driver.get(url=video_url)
#             html = driver.page_source
#             soup = BeautifulSoup(html, "html.parser")
#             play = driver.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]').text
#             play2 =str(play).split()[1]
#             print(play2)
#         except:
#             pass
       
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

# want= input()
# if "youtube" in want:
#     youtube_play(want)
# else:
#     naver_play(want)
    
################# program ####################### 
# def youtube_program(video_url):
#     try:    
#         driver.get(url=video_url)
#         html = driver.page_source
#         soup = BeautifulSoup(html, "html.parser")
#         program = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
#         print(program)
#     except:
#         print("오류발생")

        # #bs4로
        # url= requests.get(video_url)
        # soup= BeautifulSoup(url.text, "lxml")
        # title = soup.select_one('meta[itemprop="name"][content]')['content']
        # return title
                
def naver_program(video_url):
        try:
            while True:
                driver.get(video_url)
                program = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
                print(program)
        except:
            print("오류발생")

# want= input()
# if "youtube" in want:
#     youtube_program(want)
# else:
#     naver_program(want)
   