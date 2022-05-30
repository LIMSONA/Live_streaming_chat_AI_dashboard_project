from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests


def home(requests):
    return render(requests, 'home/home.html')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Create your views here.


def youtube_program(requests):
    try:    
        driver.get(url=requests)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        return print(title)
    except:
        return "오류발생"
    finally:
            driver.close()
        # #bs4로
        # url= requests.get(video_url)
        # soup= BeautifulSoup(url.text, "lxml")
        # title = soup.select_one('meta[itemprop="name"][content]')['content']
        # return title
            
def naver_program(requests):
        try:
            while True:
                driver.get(requests)
                # 영상 제목
                n_title = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
                return print(n_title)
        except:
            print("오류발생")
        finally:
            driver.close()

want= 'https://shoppinglive.naver.com/lives/541449?fm=shoppinglive&sn=home'
if "youtube" in want:
    youtube_program(want)
else:
    naver_program(want)