import pandas as pd
import numpy as np
import os
import re
import json
from konlpy.tag import Okt
import nltk
from gensim.models import FastText
from nltk.tokenize import word_tokenize
from tqdm import tqdm 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
warnings.filterwarnings(action='ignore')
tokenizer = Tokenizer()

lstm_model = load_model('/spark-work/model/fasttext_LSTM1.h5')
embedded_model = FastText.load("/spark-work/model/festtext_embedded_1.model")


# 자모분리
CHOSUNGS = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONGSUNGS = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONGSUNGS = [u'_',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',
             u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
TOTAL = CHOSUNGS + JOONGSUNGS + JONGSUNGS

def jamo_split(word, end_char="_"):
    
    result = []
    
    for char in word:
        
        character_code = ord(char)
        
        if 0xD7A3 < character_code or character_code < 0xAC00:
            result.append(char)
            continue

        chosung_index = int((((character_code - 0xAC00) / 28) / 21) % 19)
        joongsung_index = int(((character_code - 0xAC00) / 28) % 21)
        jongsung_index = int((character_code - 0xAC00) % 28)
        
        chosung = CHOSUNGS[chosung_index]
        joongsung = JOONGSUNGS[joongsung_index]
        jongsung = JONGSUNGS[jongsung_index]
        
        if jongsung_index == 0:
            jongsung = end_char
        
        result.append(chosung)
        result.append(joongsung)
        result.append(jongsung)

    return "".join(result)    
    
    
# 예측 
def test_result(s):
    try:
        if s == "" or s.isspace():
            return 0
        else:
            test_word = jamo_split(s)
            test_word_split = test_word.split()
            fast_vec = []
            for index in range(len(test_word_split)):
                if index < len(test_word_split):
                    fast_vec.append(embedded_model[test_word_split[index]])
                else:
                    fast_vec.append(np.array([0]*100))
            fast_vec = np.array(fast_vec)
            fast_vec=fast_vec.reshape(1, fast_vec.shape[0], fast_vec.shape[1])
            # 학습 데이터와 마찬가지로 3차원으로 크기 조절
            test_pre = lstm_model.predict_classes([fast_vec]) # 비속어 판별
            
            # if test_pre[0][0] == 1:
            #     return '{0} 비속어 포함!!'.format(test_pre[0][0])
            # else:
            #     return '{0} 비속어 없어요 ^.^'.format(test_pre[0][0])
            
            # 정수형으로 나와야해서 수정함
            if test_pre[0][0] == 1:
                return test_pre[0][0]
            else:
                return test_pre[0][0]
    except:
        # return "무슨 문장인지 모르겠어요~"
        
        # 비속어로 처리해야 에러들이 필터링 되어 보이지 않으니까
        return 1 
              
    # test_result(comment, embedded_model, lstm_model)
    