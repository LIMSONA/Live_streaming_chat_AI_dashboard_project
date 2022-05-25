#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
import json
from konlpy.tag import Okt
import nltk
from nltk.tokenize import word_tokenize

from tqdm import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

###### 모델 불러오기 ######

loaded_model = load_model('/spark-work/model/test-model1.h5')

###########################

okt = Okt()
tokenizer = Tokenizer()
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','을','으로','자','에','와','한','하다','부터']
max_len = 30
vocab_size = 10000
tokenizer = Tokenizer(vocab_size)

###### json 파일 불러오기 ######

with open('/spark-work/model/test3.json', encoding='utf-8') as json_file:
    vocab = json.load(json_file)
    tokenizer.word_index = vocab
    
################################

def slang_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', str(new_sentence))
    if new_sentence == "" or new_sentence.isspace():
        return '일반 댓글'
    else : 
        new_sentence = okt.morphs(new_sentence, stem=True)
        new_sentence = [word for word in new_sentence if not word in stopwords]
        if not new_sentence:
            return '일반 댓글'
        else:
            encoded = tokenizer.texts_to_sequences([new_sentence])
            pad_new = pad_sequences(encoded, maxlen = max_len)
            score = loaded_model.predict(pad_new)
            if(score > 0.2): 
                return "{0}, 비속어 포함".format(round(float(score), 2))
            else:
                return "{0}, 일반 댓글".format(round(float(1 - score), 2))