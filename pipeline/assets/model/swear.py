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

loaded_model = load_model('./test-model1.h5')

###########################

okt = Okt()
tokenizer = Tokenizer()
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','을','으로','자','에','와','한','하다','부터']
max_len = 30
vocab_size = 10000
tokenizer = Tokenizer(vocab_size)

###### json 파일 불러오기 ######

with open('./일베집합test3.json', encoding='utf-8') as json_file:
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


# In[2]:


slang_predict("근데 저게 이뻐보이나? 저 가격이면 쿠팡에서 두개 사고도 남음 ")


# In[3]:


slang_predict("헐 ㅠㅠ 너무 이쁘다 내 최애 ")


# In[4]:


slang_predict("겁나 비싸네... ")


# In[5]:


slang_predict("재미없어보여요 ")


# In[6]:


slang_predict("아메리카노 한잔에 5000원이라고? ")


# In[7]:


slang_predict("긴 댓글을 치면 비속어 분류 모델이 제대로 분류를 못하는것 같아요 ~")


# In[8]:


slang_predict("더 긴 문장을 치면 비속어 분류 모델이 분류를 잘 할까요? 길게 길게 쓰니까 임베딩이 안되서 오류가 난다고 하는건지;;              뭐때문에 오류가 나는지를 모르겠거등요... ")


# In[9]:


slang_predict("대체 어느부분에서 비속어가 포함이 되었다고 하는거죠?")


# In[10]:


slang_predict('문장을 길게 쓰면 비속어가 포함이라고 나오는건가요? 근데 이거랑 copy 파일이랑 뭐가 달라?')


# In[11]:


slang_predict("?? 왜냐고요 ㅠㅠ")

