# 이모지제거하는 정규식만 적용할 수 있도록 변경됨
# 이외 정규식지정과 불용어처리, 형태소처리등은 각자 모델에서 맞게 적용됨

import re

class c_token:  
        def preprocessing(input_str):
            re_string = re.sub('[^ A-Za-z0-9ㄱ-ㅣ가-힣!?.,]+',"", str(input_str))
            return re_string    
                      
    # 이모지만 제거 정규식 전처리
    # def preprocessing(self, input_str):
    #     re_string = re.compile("["
    #         u"\U00010000-\U0010FFFF"  #BMP characters 이외
    #                         "]+", flags=re.UNICODE).sub(r'', input_str)
        # return re_string
        
# import re
# from konlpy.tag import Okt
# from jamo import h2j, j2hcj #초성/중성/종성분리

# f = open("./stopwords-ko.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# stopwords = []
# for line in lines:
#     line = line.replace('\n', '')
#     stopwords.append(line)
# f.close()   
# 8
# class c_token:    
# # 불용어 파일 불러오기 ==> 밖에서 지정해저야 오류 안생김                         
         
# # 1 + 2 + stopword 그냥 다 합치기!
#     def preprocessing(self, input_str):
#     # 문자만 필터링
#         re_string = re.compile('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+')\
#             .sub('', input_str)
#     #형태소단위 
#         okt = Okt() #선택이유는 논문 참고
#         m_token = okt.morphs(re_string, stem=True)                                

#     # 불용어 처리
#         result = [token for token in m_token if token not in stopwords]
#         preprocessed_text= ' '.join(result)
        
#         return preprocessed_text


# # 1.문자만 필터링(이모티콘제외) & stopword(불용어)
#     def filter_str(self, input_str):
#         re_string = re.compile('[^ A-Za-z0-9ㄱ-ㅣ가-힣]+').sub('', input_str)
#         return print(re_string)
# # 2. 
# # 2-1.텍스트를 형태소 단위로 나눔
# # norm(정규화),stem(어간추출) 기본값 False
#     def m_tokenize(self, input_str):
#         okt = Okt()
#         m_token = okt.morphs(self.filter_str(input_str))
#         return print(m_token)
# #2-2. 초성/중성/종성분리
#     def c_tokenize(self, input_str):
#         c_token = j2hcj(h2j(self.filter_str(input_str)))
#         return list(c_token)

# # 형태소단위분리 & 초중종성분리
#     def cm_tokenize(self, input_str):
#         okt = Okt()
#         mm_token = okt.morphs(self.filter_str(input_str))
#         cm_token = []
#         for i in mm_token:
#             cm_token.append(self.c_tokenize(i))
#         return cm_token

# # 4.텍스트에서 명사만 ==> 워드클라우드 
# # join(형태소/품사 설명) 기본값 False
#     def noun_tokenize(self, input_str):
#         okt = Okt()
#         token = okt.nouns(self.filter_str(input_str))
#         return token