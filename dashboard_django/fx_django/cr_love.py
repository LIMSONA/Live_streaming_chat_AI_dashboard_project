from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def youtube_love(video_url):
    a=0
    while a==0:
        try:
            driver.get(url=video_url)
            love = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-formatted-string').text
            print(love)        
        except:
            pass

        
def naver_love(video_url): 
    a=0
    while a==0:
        try:
            # print("네이버")
            driver.get(url=video_url)
            love = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[3]/span[2]').text
            print(love)
        except:
            pass


want= input()
if "youtube" in want:
    youtube_love(want)
else:
    naver_love(want)
