# Jordan Kendall
# 3/3/2021
# CSS 225

import random
import math


def problem1():
    for i in range(10):
        print(random.randint(25, 35))

def problem2(gimme):
    return random.choice(gimme)

#list = [1,2,3,4]
#print(type(list))
#print(problem2(list))

def problem3():
    return random.randrange(1,100,2)

def problem4(a,b):
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    #math.pow(x,y) gives an exponent, x to the power of y.
    #math.sqrt(x) returns the square root of x.
    return c

#print(problem4(3,4))
#a = 3
#b = 4
#print(problem4(a,b))
#for i in range(10):
#print(problem3())

