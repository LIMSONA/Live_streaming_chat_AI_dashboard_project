# python 패키지 파일을 꼭 만들어서 프로젝트를 진행하도록 합니다.
# <기본적인 패키지>
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import urllib.request
from collections import Counter
import bz2
import gluonnlp as nlp
import sentencepiece
import mxnet
from tqdm import tqdm, tqdm_notebook
```

# <토치관련>
```
from sklearn.model_selection import train_test_split
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
```

# <자연어 관련>
```
import nltk
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from konlpy.tag import Mecab
from konlp.kma.klt2000 import klt2000
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer, TrainingArguments, BertModel
```

# <텐서관련>
```
import tensorflow as tf
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense, Embedding, Bidirectional, LSTM, Concatenate, Dropout
from keras.layers import Conv1D, MaxPooling1D
```
