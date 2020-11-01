*In 16_17.ipynb I tested each player 2016-17 performance with their points in the 2017-18 season. The model tried to [redict if the score was above a certain threshold.

*16_17.py is the python file with the same exact code (so that I can run from the terminal) with a for loop to iterate through different number of neighbors in the knn algorithm.


*test.ipynb learns from the performance of 2016-17 stats on 2017-18 points. It applies the learnings to the 2018-19 season to predict players that will succeed in the 2019-2020 season. 


*Variables is a file that for each score minimum determines the best k to use: the k that generates the largest difference between right and wrong results. I tried using SVC but the results were alway worst than kin, this shows that the data is still very uncleaned and the correlation is very low. 