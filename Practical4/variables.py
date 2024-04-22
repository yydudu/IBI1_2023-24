a=40
b=36
c=30
d=a-b 
e=b-c 
if d > e:
    print("The improvement from running is greater.")
    print("Running only training had a greater improvement on running time.")
elif e > d:
    print("The improvement from running and strength training is greater.")
    print("Running and strength training had a greater improvement on running time.")
else:
    print("The improvements from running only and running and strength training are equal.")
X=True
Y=False
W=(X or Y) and not (X and Y) 
print("The value of W is ",W)
# Truth table
# X      Y      W
# True   True   False
# True   False  True
# False  True   True  
# False   False False
