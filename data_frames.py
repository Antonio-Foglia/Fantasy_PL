
import pandas as pd


def data_frames(n1='2016-17.csv',n2='2017-18.csv',n3='2018-19.csv',n4='2019-20.csv',n5='2020-21.csv'):
    d16=pd.read_csv('raw_data/'+n1).set_index('full_name')
    d17=pd.read_csv('raw_data/'+n2).set_index('full_name').drop('now_cost',1)
    d18=pd.read_csv('raw_data/'+n3).set_index('full_name').drop('now_cost',1)
    d19=pd.read_csv('raw_data/'+n4).set_index('full_name').drop('now_cost',1)
    d20=pd.read_csv('raw_data/'+n5).set_index('full_name')

    #players that werent in both years are eliminated
    for n in d16.index:
        if n not in d17.index:
            d16.drop(n,0,inplace=True)

    for n in d17.index:
        if n not in d16.index:
            d17.drop(n,0,inplace=True)


    for n in d18.index:
        if n not in d19.index:
            d18.drop(n,0,inplace=True)

    for n in d19.index:
        if n not in d18.index:
            d19.drop(n,0,inplace=True)

    #anomaly
    d18.drop('Danny Ward',inplace=True)
    d19.drop('Danny Ward',inplace=True)

    #sort and reindex
    d16.sort_values('full_name',inplace=True)
    d17.sort_values('full_name',inplace=True)
    d18.sort_values('full_name',inplace=True)
    d19.sort_values('full_name',inplace=True)
    d20.sort_values('full_name',inplace=True)

    d16.reset_index(inplace=True)
    d17.reset_index(inplace=True)
    d18.reset_index(inplace=True)
    d19.reset_index(inplace=True)
    d20.reset_index(inplace=True)

    return d16,d17,d18,d19,d20
