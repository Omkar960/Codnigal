import pandas as pd
import numpy as np

exam_data = {'Name':["Anastasia","Dima","Katherine","James","Emily","Michael","Matthew","Laura","Kevin","Jonas"],'Score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],"Attempts":["yes","no","yes","no","no","yes","yes","no","no","yes"]}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data,index=labels)
print("Summary of the basic inforamtion about this DataFrame and its data: ")
print(df.info())
print('\n')
print(df)
print("\n")
print(df.dropna())
print('\n')
print(df.fillna(15,inplace=True))
print("\n")
print(df.head(7))
print('\n')
print(df.tail(5))
print('\n')
print(df.loc["e","Attempts"])
print('\n')
print(df.loc["i","Score"])