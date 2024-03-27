import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  #import functions

os.chdir("C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/practical 7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") #read the data
#some practical codes

#print(dalys_data.head())
#print(dalys_data.info())
#print(dalys_data.describe())

selected=dalys_data.iloc[0:101:10,3]  #select the DALYs from every 10th row
print(selected)

is_afghanistan=dalys_data['Entity']=='Afghanistan'
afghanistan_days=dalys_data.loc[is_afghanistan,'DALYs']
print(afghanistan_days) #select DALYs for Afghanistan

#compare china's DALYs with those in 2019

is_china=dalys_data['Entity']=='China'
china_days=dalys_data.loc[is_china,['Entity','Year','DALYs']]

mean_dalys_china = china_days['DALYs'].mean()
dalys_2019 = china_days.loc[china_days['Year']==2019,'DALYs'].iloc[0]
comparison = dalys_2019> mean_dalys_china
if comparison:
    print('The DALYs in China in 2019 was greater than the mean')
else: 
    print('The DALYs in China in 2019 was less than the mean')

plt.plot(china_days['Year'],china_days['DALYs'],'b+')
plt.xticks(china_days.Year,rotation=-90)
plt.show()
plt.clf


#question part
import seaborn as sns

data_2019=dalys_data[dalys_data['Year']==2019]

plt.figure(figsize=(6,5))
sns.boxplot(data=data_2019,x='DALYs')
plt.title('DIstribution of DALYs')
plt.xlabel('DALYs')
plt.xticks(rotation=45)
plt.show()
plt.clf
