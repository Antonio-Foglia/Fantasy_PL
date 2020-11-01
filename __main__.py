import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from data import data
from data_frames import data_frames


def main():

    again='y'
    while again=='y':
        d16,d17,d18,d19,d20=data_frames()
        train_data,train_labels=data(d16,d17,d18,d19,int(input('What is the'+
        ' points cutoff? ')))

        k=input('k (separate by space)? ').split()
        k = [ int(x) for x in k ]
        good=[]
        for k_n in k:
            model = KNeighborsClassifier(n_neighbors=k_n)
            model.fit(train_data, train_labels)

            names=d19['full_name'].to_numpy()
            test_data=d19.drop('full_name',1).to_numpy()
            predictions = model.predict(test_data)

            i=0
            while i<len(names):
                if predictions[i]==1:
                    good.append(names[i])
                i+=1

        ind=0
        great=[]
        if len(k)==1:
            great=good
        else:
            while ind < len(good):
                if good.count(good[ind])>1:
                    if good[ind] not in great:
                        great.append(good[ind])
                ind+=1

        #print(good)
        #print(great)

        results=d20.drop(['goals_scored','assists','total_points','minutes',
        'goals_conceded','creativity','influence','threat','bonus','bps',
        'ict_index','clean_sheets','red_cards','yellow_cards',
        'selected_by_percent'],1)
        for i in results.index:
            if results['full_name'][i] not in great:
                results.drop(i,inplace=True)

        print(results)
        #results.to_csv('results.csv')

        price=int(float(input('Price cutoff? '))*10)
        for i in results.index:
            if results['now_cost'][i] > price:
                results.drop(i,inplace=True)

        print(results)



        again = input("Run again? (y/n) ")


if __name__ == "__main__":
    main()
