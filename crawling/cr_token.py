import re
from konlpy.tag import Okt
from jamo import h2j, j2hcj #초성/중성/종성분리


class c_token:    
# 불용어 파일 불러오기
    global stopwords
    f = open("./crawling/stopwords-ko.txt", 'r', encoding="utf-8")
    lines = f.readlines()
    stopwords = []
    for line in lines:
        line = line.replace('\n', '')
        stopwords.append(line)
    f.close()
         
# 1 + 2 + stopword 그냥 다 합치기!
    def preprocessing(self, input_str):
    # 문자만 필터링
        re_string = re.compile('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+')\
            .sub('', input_str)
    #형태소단위 
        okt = Okt() #선택이유는 논문 참고
        m_token = okt.morphs(re_string, stem=True)
    # 초중성분리  ==> 너무 작게 쪼개져서 주석처리!!
        # cm_token = []
        # for i in m_token:
        #     cm_token.append( j2hcj(h2j(i)) )
    # 불용어 처리
        result = [token for token in m_token if token not in stopwords]
        preprocessed_text= ' '.join(result)
        
        return preprocessed_text




# 1.문자만 필터링(이모티콘제외) & stopword(불용어)
    def filter_str(self, input_str):
        re_string = re.compile('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+').sub('', input_str)
        return print(re_string)

# 2. 
# 2-1.텍스트를 형태소 단위로 나눔
# norm(정규화),stem(어간추출) 기본값 False
    def m_tokenize(self, input_str):
        okt = Okt()
        m_token = okt.morphs(self.filter_str(input_str))
        return print(m_token)
#2-2. 초성/중성/종성분리
    def c_tokenize(self, input_str):
        c_token = j2hcj(h2j(self.filter_str(input_str)))
        return list(c_token)

# 형태소단위분리 & 초중종성분리
    def cm_tokenize(self, input_str):
        okt = Okt()
        mm_token = okt.morphs(self.filter_str(input_str))
        cm_token = []
        for i in mm_token:
            cm_token.append(self.c_tokenize(i))
        return cm_token

# 4.텍스트에서 명사만 ==> 워드클라우드 
# join(형태소/품사 설명) 기본값 False
    def noun_tokenize(self, input_str):
        okt = Okt()
        token = okt.nouns(self.filter_str(input_str))
        return token



    
# 테스트하기
cl = c_token()
test = "제품은 좋을수도 있고 나쁠수도 있는데 그걸 고객들을 속이려고 하고 심지어 사과도 안하고 양심도없지"
result = cl.preprocessing(test)
print(result)
# ==> 제품 좋다 있다 나쁘다 있다 그걸 고객 속이다 하다 심지어 사과 하고 양심 없다

