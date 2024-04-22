#preudocode
#define a dictionary
#calculate the 'other' hours
#print the dictionary
#print the time spent on a randomly chosen activity
#create a pie chart

dic={"sleeping":8, "classes":6, "studying":3.5, "TV":2, "Music":1,}
otherhours = 24-sum(dic.values())
dic["other"]=otherhours
random_activity ="Music"

print (dic)
print ( "The time spent on", random_activity, "is", dic.get(random_activity), "h" )

import matplotlib.pyplot as plt
labels = dic.keys()
sizes = dic.values()
 
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.axis('equal')
plt.title('Average Day of a University Student')
plt.show()
plt.clf
