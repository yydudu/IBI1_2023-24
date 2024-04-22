density=5 #the initial density is 5%
day=0 #the initial day 
while density<=90:
    day+=1
    density =density*2  #the cell density doubles in density per day
    
print("I can stay away from lab for",day,"days")
print("On day", day,"the cell density is larger than 90%") #output the results
