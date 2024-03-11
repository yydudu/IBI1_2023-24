density=5 #the initial density is 5%
day=1 #the initial day is 1
while density<=90:
    density =density*2  #the cell density doubles in density per day
    day+=1
print("I can stay away from lab for",day,"days")
print("On day", day,"the cell density is larger than 90%") #output the results
