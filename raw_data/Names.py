import pandas as pd
df=pd.read_csv(input('name the source file:'))
df['full_name']=df['first_name']+' '+df['second_name']
df.drop('first_name',1,inplace=True)
df.drop('second_name',1,inplace=True)
df.set_index('full_name',inplace=True)
df.to_csv(input('name the destination file')+'.csv')
