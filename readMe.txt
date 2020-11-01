Fantasy PL machine learning predictor by Antonio Foglia

HOW IT WORKS:

*All the learning process can be found in testing directory.

*I train the inn algorithm with data from the 16-17 seasons and 18-19 seasons and the results of the 17-18 seasons and 19-20 seasons respectively.

*All parameters are the same weight.

*I want to find all the players that based on the previous seasons performance, score more than n points in the next season. n can be adjusted.



IMPLEMENTATION:

*__main__.py, data_frames.py and data.py are the code, sorted and cleaned. After learning from previous seasons a prediction is made for the 2020-21 season. 

*By working with the variables file, for each point total I found the k's with the highest success to failure ratio, and using those k's I determined the players that were more likely to succeed. The program does not take in account price though, I had to create a price filter in order to stay within the bounds. The final team was a mixture of predicted player and my common sense in terms of position and price management. Let's see how it performs!!


WHAT I LEARNED:

*I had to use a lot of pandas and numpy which I now feel more confident in.

*Machine learning algorithms require a great deal of data processing and cleaning.

*My program is awful since on average it only predicts less than a fifth of the players which will succeed next season. Moreover it (at bests) also predicts a tenth of players wrong.

*Improvement include sorting through the data better so that different categories have different weights. Finding hidden trends and correlations and exploiting them. More training points and a smaller time frame since fantasy is played on a weekly basis.