import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def data_frames(n1='2016-17.csv',n2='2017-18.csv',n3='2018-19.csv',n4='2019-20.csv'):
    d16=pd.read_csv('raw_data/'+n1).set_index('full_name')
    d17=pd.read_csv('raw_data/'+n2).set_index('full_name')
    d18=pd.read_csv('raw_data/'+n3).set_index('full_name')
    d19=pd.read_csv('raw_data/'+n4).set_index('full_name')
    d19=pd.read_csv('raw_data/'+n4).set_index('full_name')
