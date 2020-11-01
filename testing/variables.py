#This file uses output data to try and optimize the best method to use and which
#parameters to use. The methods used are the same as the test.ipynb file

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def frames():
    d16=pd.read_csv('../raw_data/2016-17.csv').set_index('full_name')
    d17=pd.read_csv('../raw_data/2017-18.csv').set_index('full_name').drop('now_cost',1)
    d18=pd.read_csv('../raw_data/2018-19.csv').set_index('full_name').drop('now_cost',1)
    d19=pd.read_csv('../raw_data/2019-20.csv').set_index('full_name').drop('now_cost',1)

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

    d18.drop('Danny Ward',inplace=True)
    d19.drop('Danny Ward',inplace=True)

    d16.sort_values('full_name',inplace=True)
    d17.sort_values('full_name',inplace=True)
    d18.sort_values('full_name',inplace=True)
    d19.sort_values('full_name',inplace=True)

    d16.reset_index(inplace=True)
    d17.reset_index(inplace=True)
    d18.reset_index(inplace=True)
    d19.reset_index(inplace=True)

    return d16,d17,d18,d19

def data(pts,d16,d17,d18,d19):
    train_data=d16.drop('full_name',1).to_numpy()
    train_labels=d17['total_points'].to_numpy()
    i=0
    while i<len(train_labels):
        if train_labels[i]<pts:
            train_labels[i]=0
        else:
            train_labels[i]=1
        i+=1

    test_data=d18.drop('full_name',1).to_numpy()
    test_labels=d19['total_points'].to_numpy()
    i=0
    while i<len(test_labels):
        if test_labels[i]<pts:
            test_labels[i]=0
        else:
            test_labels[i]=1
        i+=1

    return train_data,train_labels,test_data,test_labels

def knn(train_data,train_labels,test_data,test_labels,k):

    model = KNeighborsClassifier(n_neighbors=k,weights='distance')
    model.fit(train_data, train_labels)
    predictions = model.predict(test_data)

    return diff(predictions,test_labels)

def svc(train_data,train_labels,test_data,test_labels):

        model = SVC()
        model.fit(train_data, train_labels)
        predictions = model.predict(test_data)

        return diff(predictions,test_labels)

def diff(predictions,test_labels):
    i=0
    number=0
    right=0
    bad=0
    while i< len(predictions):
        if test_labels[i]==1:
            number+=1
            if predictions[i]==1:
                right+=1

        if test_labels[i]==0 and predictions[i]==1:
            bad+=1

        i+=1

    return right,bad,number

def main():

    d16,d17,d18,d19=frames()
    diff_knn=0
    right_knn=0
    bad_knn=0
    number_knn=0
    best_pts_knn=0
    best_k=0

    diff_svc=0
    right_svc=0
    bad_svc=0
    number_svc=0
    best_pts_svc=0

    for pts in range(int(input('Lower band? ')),201,1):
        train_data,train_labels,test_data,test_labels=data(pts,d16,d17,d18,d19)
        for k in range(1,31,1):
            right,bad,number = knn(train_data,train_labels,test_data,test_labels,k)
            diff=right-bad
            if diff>10:
                print("knn  pts: %d  k: %d  r: %d  b: %d  n: %d  diff: %d" %(pts,k,right,bad,number,diff))
            if diff > diff_knn:
                diff_knn=diff
                right_knn=right
                bad_knn=bad
                number_knn=number
                best_pts_knn=pts
                best_k=k


        # right,bad,number = svc(train_data,train_labels,test_data,test_labels)
        # diff=right-bad
        # if diff>10:
        #     print("svc  pts: %d  r: %d  b: %d  n: %d  diff: %d" %(pts,right,bad,number,diff))
        # if diff > diff_svc:
        #     diff_svc=diff
        #     right_svc=right
        #     bad_svc=bad
        #     number_svc=number
        #     best_pts_svc=pts




    print("Best knn  pts: %d  k: %d  r: %d  b: %d  n: %d  diff: %d" %(best_pts_knn,best_k,right_knn,bad_knn,number_knn,diff_knn))
    # print("Best svc  pts: %d  r: %d  b: %d  n: %d  diff: %d" %(best_pts_svc,right_svc,bad_svc,number_svc,diff_svc))

    return


main()
