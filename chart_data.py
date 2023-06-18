import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st


iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)


#데이터 표시
df1_lists = [f for f in df_lists if f.endswith('.csv')]
print("Df1 Lists : ", df1_lists)


#데이터 나누기
data_lists = [filename for filename in df1_lists if filename != 'kemp-process-rate.csv']
error_list = 'kemp-process-rate.csv'

print("Data Lists : ", data_lists)
print("Error Data List : ", error_list)


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
