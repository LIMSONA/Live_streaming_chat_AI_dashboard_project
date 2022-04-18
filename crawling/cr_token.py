import re
from konlpy.tag import Okt
from jamo import h2j, j2hcj #초성/중성/종성분리


class c_token:
# 1.문자만 필터링(이모티콘제외)
    def filter_str(self, input_str):
        re_string = re.compile('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+').sub('', input_str)
        return re_string

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

# 형태소단위분리 & 초중성분리
    def cm_tokenize(self, input_str):
        okt = Okt()
        mm_token = okt.morphs(self.filter_str(input_str))
        cm_token = []
        for i in mm_token:
            cm_token.append(self.c_tokenize(i))
        return cm_token


# 3.텍스트에서 명사만 ==> 워드클라우드 
# join(형태소/품사 설명) 기본값 False
    def noun_tokenize(self, input_str):
        okt = Okt()
        token = okt.nouns(self.filter_str(input_str))
        return token
    

a= "집에 가고 싶다.... ㅋㅋㅋㅋ★"

c_token.m_tokenize(a)