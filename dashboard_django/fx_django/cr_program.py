from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def youtube_program(video_url):
    try:    
        driver.get(url=video_url)
        program = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        print(program)
    except:
        print("오류발생")

        
        
def naver_program(video_url):
        try:
            driver.get(video_url)
            program = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
            print(program)
        except:
            print("오류발생")



want= input()
if "youtube" in want:
    youtube_program(want)
else:
    naver_program(want)
