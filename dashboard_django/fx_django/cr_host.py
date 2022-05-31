from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup 

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def youtube_host(video_url):
    try:
        driver.get(url=video_url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # host = driver.find_element_by_class_name("yt-simple-endpoint style-scope yt-formatted-string").text
        host = driver.find_element_by_xpath('//*[@id="text"]/a').text
        print(host)
    except:
        print("오류발생")
        
        
def naver_host(video_url):   
    try:
        driver.get(url=video_url)
        host = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[1]').text
        print(host)
    except:
        print("오류발생")


want= input()
if "youtube" in want:
    youtube_host(want)
else:
    naver_host(want)
