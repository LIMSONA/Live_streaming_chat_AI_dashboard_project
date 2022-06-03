#!/usr/bin/env python
# coding: utf-8

# ## spark udf 테스트

# In[1]:


import pandas as pd
import numpy as np
import re
import json
from konlpy.tag import Okt
import nltk # 자연어 처리 패키지
from gensim.models import FastText
from nltk.tokenize import word_tokenize
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import warnings
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
warnings.filterwarnings(action='ignore')


lstm_model = load_model('/spark-work/model/fasttext_LSTM2.h5')
embedded_model = FastText.load("/spark-work/model/festtext_embedded_2.model")


# 자모분리
CHOSUNGS = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONGSUNGS = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONGSUNGS = [u'_',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
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
            test_pre = lstm_model.predict_classes([fast_vec])

            if test_pre[0][0] == 1:
                return int(test_pre[0][0])
            else:
                return int(test_pre[0][0])
    except:
        return 0
# 빈 값이나 이모티콘같은 경우 비속어로 분류되면 안되기 때문에 0

# In[ ]:




