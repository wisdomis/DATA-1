# app.py

import streamlit as st
#from sklearn.datasets import load_iris 
#from PIL import Image
from time import sleep

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
#from sklearn import tree
#import seaborn as sns
#from sklearn.metrics import mean_squared_error
from math import sqrt
#from sklearn.metrics import mean_squared_error
#from sklearn.model_selection import train_test_split
from math import sqrt
#from sklearn.metrics import confusion_matrix
#from sklearn.metrics import accuracy_score
#from sklearn.metrics import precision_score
#from sklearn.metrics import recall_score
#from sklearn.metrics import f1_score
#from sklearn.metrics import roc_curve
#from sklearn.metrics import classification_report




#st.title('데이터보')

DATA_URL = ('')



# 페이지 기본 설정
st.set_page_config(
    page_icon="🏫",
    page_title="생산시스템구축실무 데이터보팀",
    layout="wide",
)

# 로딩바 구현하기
with st.spinner(text="페이지 로딩중..."):
    sleep(2)

# 페이지 헤더, 서브헤더 제목 설정
st.header("생산시스템구축실무 데이터보팀")
st.subheader("공정운영 최적화 데이터 분석")

# 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
cols = st.columns((1,))
cols[0].metric("10/11", "15 °C", "2")



# 라인 그래프 데이터 생성(with. Pandas)


chart_data = pd.DataFrame(
    np.random.randn(20, 1),
    column=['time'],
    raws=['PH','temp'] )


df = pd.read_csv('./dataset/kemp-process-rate.csv', encoding='cp949')