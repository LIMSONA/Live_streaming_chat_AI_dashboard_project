from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django.http import HttpResponse, JsonResponse
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# def youtube_host(video_url):
#     try:
#         driver.get(url=video_url)
#         host = driver.find_element_by_xpath('//*[@id="text"]/a').text
#         print(host)
#     except:
#         print("오류발생")
        
        
def naver_host(request): 
    # try:
    url = urllib.parse.unquote(request.GET.get("url"))
    driver.get(url=url)
    
    
    host = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/header/div/a[2]/div/span[1]').text
    
    loveElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/div/span[3]/span[2]'))
    )
    
    love = loveElement.text
    
    playElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/div/span[2]/span[2]'))
    )
    play = playElement.text
    
    program = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/header/div/a[2]/h2').text
    
    chatContainerElement = driver.find_element_by_css_selector('#root > div > div > div > div > div > div > div > div[class^=Comments_wrap] > div > div:nth-child(1)')
    chatElements = chatContainerElement.find_elements(By.XPATH, "*")

    chats = []
    for item in chatElements :
        elements = item.find_elements(By.XPATH, "*");
        chats.append({ "nickName" : elements[0].text, "contents" : elements[1].text })
    
    # <div class="">
    #     <strong role="presentation" class="Comment_id_3pR4u">자몽자몽</strong>
    #     <span role="presentation" class="Comment_comment_2d0tc"> 가격 혜택 좋네요</span>
    # </div>
    
    data = {
        "host" : host,
        "love" : love,
        "play" : play,
        "program" : program,
        "chats" : chats
    }
    return JsonResponse(data)
    # except:
    #     return HttpResponse("error");



# want= input()
# if "youtube" in want:
#     youtube_host(want)
# else:
#     naver_host()
