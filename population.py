from individual import INDIVIDUAL
import copy
import constants as c
import random
import math
import numpy
class POPULATION:
    def __init__(self, popSize):
        self.p = {}  
        self.popSize= popSize
        self.bestParentIndex = 0
    def Initialize(self): 
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i)  
                
    def Evaluate(self, envs, pp, pb):
        for i in self.p:
            self.p[i].fitness = 0
        for e in range(0, c.numEnvs):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp,pb)
            for i in self.p:
                self.p[i].Compute_Fitness()              
        for i in self.p:
            self.p[i].fitness /= c.numEnvs  
    def Print(self):
        for i in self.p:
            if ( i in self.p ):
                self.p[i].Print()
        print()
    
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in self.p:
            if(self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]
                
    def Get_Data(self):
        result = []
        for i in self.p:
            result.append(self.p[i].fitness)
            return result[-1]
    
    def Fill_From(self, other): 
        self.Copy_Best_From(other)
        print("this is the best individual: ")
        #self.Print()
        self.Collect_Children_From(other)
        #self.Print()

    def Copy_Best_From(self, other):
        highestval = -2.0
        for i in other.p:
            if (other.p[i].fitness > highestval):
                self.bestParentIndex = i
                highestval = other.p[i].fitness
        self.p[0] = copy.deepcopy(other.p[self.bestParentIndex])

        
    def Collect_Children_From(self,other):
        h = self.bestParentIndex
        i = 1

        

        for j in other.p:
            if (j != h):
                #winner  
                #self.p[i] = copy.deepcopy(other.Winner_Of_Tournament_Selection())
                #bestOtherParent = other.p[j]

                bestOtherParent = self.Winner_Of_Tournament_Selection(other)
                self.p[i] = copy.deepcopy(other.p[bestOtherParent])
                self.p[i].Mutate()
                i += 1
                
            
            
    def Winner_Of_Tournament_Selection(self, other):
        #val = self.popSize
        lent = len(other.p)
        
        p1 = random.randint(0, lent  - 1)
        p2 = random.randint(0, lent - 1)

        while( p1==p2 ):  
            p1 = random.randint(0, lent - 1)
            p2 = random.randint(0, lent - 1)

        if( other.p[p1].fitness > other.p[p2].fitness ):
             
            bestParentIndex = p1 
        else:
            bestParentIndex = p2
        
        return bestParentIndex

            