from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime


okt= Okt()

bucket= []

def c_wordcloud(sentence):
    morph= okt.nouns(sentence)
    for i in morph:
        bucket.append(i)
    
    counts= Counter(bucket)
    
    wc= WordCloud(font_path='malgun', width=400, height=400, 
                  scale=2.0, max_font_size=250)
    gen= wc.generate_from_frequencies(counts)
    # plt.figure()
    # plt.imshow(gen)
    time= datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    # plt.savefig('c_wordcloud_{time}.png')
    gen.to_file("./crawling/c_wordcloud_{}.png".format(time))



#테스트 완료

# msg= "'메시지는 차치하고 감각적으로(시각, 청각) 황홀했다. 영화는 가능하고, 소설은 불가능한 것. 영화는 도달할 수 있고, 소설은 도달할 수 없는 것. 영화는 체험시킬 수 있고, 소설은 체험시킬 수 없는 것. 더 확장하면...', '개봉일을 기다려, 모처럼 팔순의 친정어머니와 롯데 시네마에서 보았어요. 잔잔한 시냇물이 흐르는 계곡에 미나리 밭을 일구는 우리들의 어머니 또는 할머니의 강인한 생존력이란! 대지의 후손들이라면 누구나 배꼽 아래 단전으...', '하....  이것이 제 심사평입니다. 이런 게 바로 영화 아니겠습니다. 오늘 하루 하.. 할듯..', '평양냉면 같은 영화. 막상 기대했다가 보면 이게뭐야? 할지도 모르지만 극장을 나선 뒤에도 잔잔하게 울림을 주는 영화', '이 영화자체가 미나리같다. 그리고 이 영화에 나오는 인물들도 미나리같다. 특별하고 화려하진 않지만 강인하고  자꾸 머릿속에 이 가족의 현재와 미래가 궁금해지고 응원하게 된다.그들의 모습속에서 가장으로써의 모습, 어머...'"
# c_wordcloud(msg)

    