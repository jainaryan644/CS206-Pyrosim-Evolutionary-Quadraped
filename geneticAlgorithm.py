import pyrosim
import copy
import constants as c
import pickle
import random
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION
from environments import environments 

envs = environments(0)
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp = False, pb= True)
print('0', end = '')
parents.Print()

for g in range(1, c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp = False, pb = True)
    print(g, end = '')
    children.Print()
    parents.ReplaceWith(children)
    
parents.Evaluate(envs, pp= False, pb= False)



    #children = copy.deepcopy(parents)
   # children.Mutate()
   # children.Evaluate(True)
   # parents.ReplaceWith(children)
  #  print(g, end='')
  #  parents.Print()
#parents.Evaluate(False)
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