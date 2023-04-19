import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
# function in which GA is to applied or can be said it is the function to be optimised
def problem (x,y,z):
    return 6*x**3 + 9*y**2 + 9*z - 25



# fitess function to check wheather the parameters used is good or not
def fitness (x,y,z):
    ans = problem(x,y,z)

    if ans == 0:
        return 99999; # this  how good the parameter is
    else:
        return abs(1/ans) # more closer to 0 value is i.e. more better it is higher will be the value for the ans



# generate a total of 1000 solutuions for the problem (also can be said population)
solutions = []
for s in range(1000):
    solutions.append( ( random.uniform(0,1000),
                        random.uniform(0,1000),
                        random.uniform(0,1000) ) )  #xyz is generated here with any value within the given interval[0,1000] is equally likely to be selected



# generate solutions for 10000 times/generation without crossover and mutation
for i in range(10000):
    rankedsolutions = [] #contains parameters, index/generation
    for s in solutions:
         rankedsolutions.append( (fitness(s[0],s[1],s[2]),s)) #xyz is sent to the fitness function
    rankedsolutions.sort()
    rankedsolutions.reverse() #best solution is created and sorted with 1 been th best one

    print(f"__________ Generation {i} Best Solutions Without C&M __________")
    print(rankedsolutions[0])
    print(' ') 


# generate solutions for 10000 times/generation with crossover and mutation
for i in range(10000):
    rankedsolutions = []
    for s in solutions:
         rankedsolutions.append( (fitness(s[0],s[1],s[2]),s)) #xyz is sent to the fitness function
    rankedsolutions.sort()
    rankedsolutions.reverse() #best solution is created and sorted with 1 been th best one

    print(f"__________ Generation {i} Best Solutions With C&M__________")
    print(rankedsolutions[0])
    print(' ') 

    if rankedsolutions[0][0] > 99999:
        break;

    bestsolutions = rankedsolutions[0:50] #this will hold the parameters which gave the best solutions
    elements_0 = []
    elements_1 = []
    elements_2 = []
    for s in bestsolutions:
        elements_0.append(s[1][0])
        elements_1.append(s[1][1])
        elements_2.append(s[1][2])
 
    newgen = []
    for x in range(1000): #choose the randomly three value for the paraameters and mutate by 2%
        e1 = random.choice(elements_0) * random.uniform(0.99,1.01)
        e2 = random.choice(elements_1) * random.uniform(0.99,1.01)
        e3 = random.choice(elements_2) * random.uniform(0.99,1.01)

        newgen.append((e1,e2,e3))
    
    solutions = newgen