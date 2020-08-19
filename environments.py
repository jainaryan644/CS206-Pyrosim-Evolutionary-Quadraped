import constants as c
from environment import environment


class environments: 
    def __init__(self, sim):
        
        
        self.envs = {}

        for e in range ( 0, c.numEnvs): 

            self.envs[e] = environment(e)
    
    
        