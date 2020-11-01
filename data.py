import numpy as np
import pandas as pd


def data(d16,d17,d18,d19,points=100):
    data1=d16.drop('full_name',1).to_numpy()
    data2=d18.drop('full_name',1).to_numpy()

    labels1=d17['total_points'].to_numpy()
    i=0
    while i<len(labels1):
        if labels1[i]<points:
            labels1[i]=0
        else:
            labels1[i]=1
        i+=1

    labels2=d19['total_points'].to_numpy()
    i=0
    while i<len(labels2):
        if labels2[i]<points:
            labels2[i]=0
        else:
            labels2[i]=1
        i+=1

        train_data=np.concatenate((data1,data2))
        train_labels=np.concatenate((labels1,labels2))

        return train_data,train_labels
