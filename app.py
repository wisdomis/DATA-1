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
cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")

cols[0].metric("10/13", "15 °C", "2")

cols[1].metric("10/15", "14 °C", "-3 °F")


# 라인 그래프 데이터 생성(with. Pandas)

df = os.getcwd()
df_lists = os.listdir(df)
print("Df Lists : ", df_lists)


#데이터 조합화
def csv_read_(data_dir, data_list):
    tmp = pd.read_csv(os.path.join(data_dir, data_list), sep=',', encoding='UTF8')
    y, m, d = map(int, data_list.split('-')[-1].split('.')[:-1])
    time = tmp['Time']
    tmp['DTime'] = '-'.join(data_list.split('-')[-1].split('.')[:-1])
    ctime = time.apply(lambda _: _.replace(u'오후', 'PM').replace(u'오전', 'AM'))
    n_time = ctime.apply(lambda _: datetime.datetime.strptime(_, "%p %I:%M:%S"))
    newtime = n_time.apply(lambda _: _.replace(year=y, month=m, day=d))
    tmp['Time'] = newtime
    return tmp

#chart_data = pd.DataFrame(
    #np.random.randn(20, 3),
    #columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)

import datetime
import streamlit as st

d = st.date_input(
    "TODAY",
    datetime.date(2023, 6, 20))
st.write('TODAY:', d)


cols[1].line_chart(chart_data)



# 특정 시간 범위 설정
start_time = pd.to_datetime('2021-09-10 09:01:18')
end_time = pd.to_datetime('2021-09-10 10:30:00')

# 해당 시간 범위의 데이터 추출
subset = X_data[(X_data.index >= start_time) & (X_data.index <= end_time)]

# 온도와 품질 그래프
plt.figure(figsize=(10,5))
plt.plot(subset.index, subset['pH'], color='tab:blue', label='pH')
plt.plot(subset.index, subset['Process'], color='tab:red', label='Process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time vs pH/Process')
plt.legend()
plt.show()
