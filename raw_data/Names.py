#This file joins the names of the players to a single cell

import pandas as pd
df=pd.read_csv(input('name the source file:')+'.csv')
df['full_name']=df['first_name']+' '+df['second_name']
df.drop('first_name',1,inplace=True)
df.drop('second_name',1,inplace=True)
df.set_index('full_name',inplace=True)
df.to_csv(input('name the destination file')+'.csv')
