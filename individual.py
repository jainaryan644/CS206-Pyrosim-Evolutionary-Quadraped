import random
import math
import constants as c
import numpy as np
import pyrosim
from environment import environment
from robot import ROBOT
class INDIVIDUAL:
    def __init__(self, i):
        self.genome = self.genome = np.random.random(size =(5,8)) * 2 - 1
        self.fitness=0
        self.ID=i
            
    def Start_Evaluation(self, env, pp, pb):
        
        self.sim = pyrosim.Simulator( play_paused = pp, eval_time = c.evalTime, play_blind = pb ) #instantiates the simulator
        env.Send_To(self.sim)
        self.robot = ROBOT( self.sim, self.genome )
        
        self.sim.start()
        

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        z = self.sim.get_sensor_data( sensor_id = self.robot.L4 , svi = 0 )
        self.fitness += z[-1] 
        #self.fitness = 0.888888888888
        del self.sim
        

    def Mutate(self):
        rowToMutate = random.randint(0,len(self.genome) - 1)
        colToMutate = random.randint(0, len(self.genome[0]) -1)
        #geneToMutate = random.randint(0,3)
        self.genome[rowToMutate][colToMutate] = random.gauss(self.genome[rowToMutate][colToMutate] , math.fabs(self.genome[rowToMutate][colToMutate]))
        #self.genome[rowToMutate][colToMutate] = 2

    def Print(self):
        print('[', self.ID, ' ', self.fitness, ']', end = ' ')
