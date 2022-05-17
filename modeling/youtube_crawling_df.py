import pytchat
import time
from datetime import datetime, timedelta
import pandas as pd
import os

time = datetime.now().strftime("%Y-%m-%d")
current = datetime.now()
two_minutes_later = current + timedelta(minutes=2)
ten_minutes_later = current + timedelta(minutes=10)
half_hour_later = current + timedelta(minutes=30)


num= 0
def youtube_cr():
    chat = pytchat.create(video_id="py_phbQxy5Y")
    while chat.is_alive():
        for c in chat.get().sync_items():
            df = pd.DataFrame()
            df["comment"]= [c.message]
            address= "C:\crawling\\youtube\\"   
            file_name = os.path.join(address + f"{time}.csv")
            
            if os.path.exists(file_name):
                prev_df = pd.read_csv(file_name)
                result = pd.concat([prev_df,df], axis=0)
        # ID와 내용 기준으로 중복되는 것 DROP 시키고, 첫번째는 남기는 조건, 인덱스 재정렬
                re_result= result.drop_duplicates(["comment"], keep="first", ignore_index= True)
        # 다시 저장하기!
                re_result.to_csv(file_name, index= False)   
            else:
                df.to_csv(file_name, index= False)               
    return df

while True:
    try:
        youtube_cr()
    except:
        print("오류발생")
        pass
    currentTime = datetime.now()
    if (half_hour_later <= currentTime):
        break
