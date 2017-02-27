# Author: Parker Haggerty
# Date: 2/7/17
# Assignment 2, Problem 1


from math import sqrt

# Variables
c = 3.0*(10**8) #meters/sec
x = int(input("Please enter a distance in light years: \n"))
v = float(input("Please enter a velocity as a fraction of the speed of light, c: \n"))
xm = x*(9.461*(10**15)) #converts distance to meters


# To find time perceived by passenger:
proper_time = xm/c
print("Time perceived by passenger is:", proper_time)


# To find gamma
gamma = 1/sqrt(1-(((v*c)**2)/(c**2)))
print("Gamma is:", gamma)
print("\n")


#To find time in rest frame (observer from Earth)
t = proper_time*gamma
print("Time, as observed from Earth, is:", t)


            # Results #

# Part a: time as perceived from rest frame:
# Results for x=10 light years...
# For v=0.90c, t = 723500752.7164618 seconds
# For v=0.98c: t = 1584777128.361235 seconds
# For v=0.999c: t = 7053576659.686199


# Part b: time as perceived by a passenger:
# Results for x=10 light years...
# For v=0.90c, proper_time = 315366666.6666667 seconds
# For v=0.98c: proper_time = 315366666.6666667 seconds
# For v=0.999c: proper_time = 315366666.6666667