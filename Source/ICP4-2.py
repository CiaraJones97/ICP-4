import numpy as np

# Make a 10,10 array and fill it with random numbers between 0 and 99
x = np.random.randint(0,100,(10, 10))
print(x)

# Find the maximum and minimum values for the row
for i in range (0,10):
    print("Row {} max value is {}".format(i,x[i,:].max()))
    print("Roe {} min value is {}".format(i,x[i,:].min()))

