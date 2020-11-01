Fantasy PL machine learning predictor.

In 16_17.ipynb I tested each player 2016-17 performance with their points in the 2017-18 season. The model tried to [redict if the score was above a certain threshold.

16_17.py is the python file with the same exact code (so that I can run from the terminal) with a for loop to iterate through different number of neighbors in the knn algorithm.


test.ipynb learns from the performance of 2016-17 stats on 2017-18 points. It applies the learnings to the 2018-19 season to predict players that will succeed in the 2019-2020 season. It did this on average with 87% accuracy. 

__main__.py, data_frames.py and data.py are the code, sorted and cleaned. After learning from previous seasons a prediction is made for the 2020-21 season. 
