# Below, some doodlings to learn Python with Maddy
# Resources:
#   https://www.w3schools.com/python/default.asp  - free, no nonsense site, for learning many different languages, inc Python
#   https://www.python.org/about/ - The authoratitive python site (not spent much time here)

# Print statement explained here: https://www.w3schools.com/python/ref_func_print.asp
print("Hello, Mad!")

# Tuples explained: https://www.w3schools.com/python/python_tuples.asp
myTuple = (1,1,"Low") 

# Print the Tuple  this will print all values within the tuple
print("myTuple=", myTuple)

# Access individual elements within the Tuple. See https://www.w3schools.com/python/python_tuples_access.asp
print("Value1=", myTuple[0], "Value2=", myTuple[1], "Risk=",myTuple[2])

# Create a list of Tuples. Lists explained: https://www.w3schools.com/python/python_lists.asp
myListOfTuples = [(1,1),(1,2)]
print("List of tuples:", myListOfTuples)

# Loop through the list of tuples. For loop info: https://www.w3schools.com/python/python_for_loops.asp
for tuple in myListOfTuples:
    print(tuple)
