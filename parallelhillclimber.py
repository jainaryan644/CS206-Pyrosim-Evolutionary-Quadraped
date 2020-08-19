import pyrosim
import copy
import pickle
import random
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION
size = 10
if size > 0:
    parents = POPULATION(size)
    parents.Initialize()
    parents.Evaluate(True)
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(1, end = '')
    parents.Print()
else:
    print('Check the size of Population. It has to be non zero and non negative number')
for g in range(2, 200):
    children.Initialize()
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(g, end='')
    parents.Print()
parents.Evaluate(False)
#class PARENT():
#parent = INDIVIDUAL()
#parent.Evaluate(True)
#   for i in range(0,50):
#       child = copy.deepcopy( parent ) 
#       child.Mutate()
#       child.Evaluate(True)
#       print("[currgen: ", i, "]", "[weight: ", parent.genome, "]", "[p:" , parent.fitness , "]", "[c: ", child.fitness, "]")
#       if ( child.fitness > parent.fitness ):
#           parent = child