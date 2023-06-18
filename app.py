# app.py

import streamlit as st
import pandas as pd
import numpy as np
#from sklearn.datasets import load_iris 
from PIL import Image
from time import sleep

import streamlit as st

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
cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")

cols[0].metric("10/13", "15 °C", "2")

cols[1].metric("10/15", "14 °C", "-3 °F")


# 라인 그래프 데이터 생성(with. Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)

import datetime
import streamlit as st

d = st.date_input(
    "DAY",
    datetime.date(2023, 6, 20))
st.write('DAY:', d)





iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
return species_dict[x]

