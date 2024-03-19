uk_cities =[0.56,0.62,0.04,9.7]
China_cities =[0.58,8.4,29.9,22.2]
print(uk_cities)
print(China_cities)

import matplotlib.pyplot as plt
import numpy as np

fig,(ax,ax1)=plt.subplots(1,2,figsize=(10,5))

UK_city_names =["Edinburgh",'Glasgow', 'Stirling', 'London']
bar_colors = ['tab:red','tab:blue','tab:orange','tab:purple']
ax.bar(UK_city_names,uk_cities,label= uk_cities, color=bar_colors )
ax.set_ylabel('population')
ax.set_title('The Poplulation of Cities in UK')

China_city_names =['Haining','Hangzhou','Shanghai','Beijing']
ax1.bar(China_city_names,China_cities,label=China_cities,color=bar_colors)
ax1.set_ylabel('population')
ax1.set_title('The Poplulation of Cities in China')

plt.show()
plt.clf
