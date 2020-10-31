

import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


def hello(neg,s):
    d16=pd.read_csv('raw_data/2016-17.csv').set_index('full_name')
    d17=pd.read_csv('raw_data/2017-18.csv').set_index('full_name')

    #Eliminating all players that dint play in both years
    #sorting alphabetically

    for n in d16.index:
        if n not in d17.index:
            d16.drop(n,0,inplace=True)

    for n in d17.index:
        if n not in d16.index:
            d17.drop(n,0,inplace=True)




    d16.sort_values('full_name',inplace=True)
    d17.sort_values('full_name',inplace=True)

    d16.reset_index(inplace=True)
    d17.reset_index(inplace=True)

    labels=d17['total_points'].to_numpy()
    i=0
    while i<len(labels):
        if labels[i]<110:
            labels[i]=0
        else:
            labels[i]=1
        i+=1


    names=d16['full_name'].to_numpy()

    data=d16.drop('full_name',1).to_numpy()

    train_data=data[:s]
    train_labels=labels[:s]
    test_data=data[s:]
    test_labels=labels[s:]

    model = KNeighborsClassifier(n_neighbors=neg)

    model.fit(train_data, train_labels)

    predictions = model.predict(test_data)

    results=pd.DataFrame()

    results['name']=names[s:]

    results['actual']=test_labels
    results['predicted']=predictions

    return sum(predictions == test_labels)/len(test_labels)


def main():
    num=310
    i=1
    print(num)
    while i<10:
        print('k='+str(i)+'||perc:'+str(hello(i,num)))
        i+=1

if __name__ == "__main__":
    main()
