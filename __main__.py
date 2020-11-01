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
        'points cutoff? ')))

        model = KNeighborsClassifier(n_neighbors=int(input('Neighbours? ')))
        model.fit(train_data, train_labels)

        names=d19['full_name'].to_numpy()
        test_data=d19.drop('full_name',1).to_numpy()
        predictions = model.predict(test_data)

        good=[]
        i=0
        while i<len(names):
            if predictions[i]==1:
                good.append(names[i])
            i+=1

        print(good)

        results=d20.drop(['goals_scored','assists','total_points','minutes',
        'goals_conceded','creativity','influence','threat','bonus','bps',
        'ict_index','clean_sheets','red_cards','yellow_cards',
        'selected_by_percent'],1)
        for i in results.index:
            if results['full_name'][i] not in good:
                results.drop(i,inplace=True)


        print(results)

        again = input("Run again? (y/n) ")


if __name__ == "__main__":
    main()
