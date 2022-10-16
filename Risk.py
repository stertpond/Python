# This is the original method
def Risk(value1, value2):
 if(value1 == 1 and value2 == 1): return 'Low'
 if(value1 == 1 and value2 == 2): return 'Low'
 if(value1 == 1 and value2 == 3): return 'Medium'
 if(value1 == 1 and value2 == 4): return 'Medium'
 if(value1 == 2 and value2 == 1): return 'Low'
 if(value1 == 2 and value2 == 2): return 'Medium'
 if(value1 == 2 and value2 == 3): return 'Medium'
 if(value1 == 2 and value2 == 4): return 'High'
 if(value1 == 3 and value2 == 1): return 'Medium'
 if(value1 == 3 and value2 == 2): return 'Medium'
 if(value1 == 3 and value2 == 3): return 'High'
 if(value1 == 3 and value2 == 4): return 'High'
 else: return 'No risk'

# This is our new more efficient method
def Risk2(value1, value2):
 if(value1 == 1 and (value2 == 1 or value2==2)): return 'Low'
 if(value1 == 1 and (value2 == 3 or value2==4)): return 'Medium'
 if(value1 == 2 and value2 == 1): return 'Low'
 if(value1 == 2 and (value2 == 2 or value2== 3)): return 'Medium'
 if(value1 == 2 and value2 == 4): return 'High'
 if(value1 == 3 and (value2 == 1 or value2 == 2)): return 'Medium'
 if(value1 == 3 and (value2 == 3 or value2==4)): return 'High'
 else: return 'No risk'

# The code below checks that both the orinal method (Risk) and the new method (Risk2) both return the expected Risk 
# for all the different values

# First, we define a list of 'tuples'. A tuple is an object that is used to store multiple values
# Each of our tuples contain 3 objects corresponding to, Value1, Value2 and the expected Risk
# For example, tuple (1,1,'Low') has Value1=1, Value2=2 and the expected risk is 'Low'
# Put all of the tuples we are interested in into a list (list are defined by the square brackets)
tuples = [(1,1,'Low'),(1,2,'Low'),(1,3,'Medium'),(1,4,'Medium')
,(2,1,'Low'),(2,2,'Medium'),(2,3,'Medium'),(2,4,'High')
,(3,1,'Medium'),(3,2,'Medium'),(3,3,'High'),(3,4,'High')
]

# Loop through all of tuples in the list and test each method against the tuble values
for tuple in tuples:
    v1=tuple[0] # extract Value1 from the tuple
    v2=tuple[1] # extract value 2 from the tuple
    expectedRisk=tuple[2] #extract expected Risk from the tuple
    
    risk = Risk(v1,v2) # calculate the Risk using original method
    if (risk!=expectedRisk) : # verify that first method has returned correct Risk
        print ("ERROR! Risk is incorrect for values:",v1,v2,expectedRisk, risk)
    
    risk2 = Risk2(v1,v2) # calculate the Risk using our new method
    if (risk2!=expectedRisk) : # verify that the new  method has returned correct Risk
        print ("ERROR! Risk2 is incorrect for values:",v1,v2,expectedRisk, risk)

    print(tuple, risk, risk2)
    continue
