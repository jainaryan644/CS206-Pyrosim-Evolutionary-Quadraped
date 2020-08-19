import pyrosim
import copy
import pickle
import random
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
class PARENT():
    parent = INDIVIDUAL()
    parent.Evaluate(True)
    for i in range(0,50):
        child = copy.deepcopy( parent ) 
        child.Mutate()
        child.Evaluate(True)
        print("[currgen: ", i, "]", "[weight: ", parent.genome, "]", "[p:" , parent.fitness , "]", "[c: ", child.fitness, "]")
        if ( child.fitness > parent.fitness ):
            parent = child
            #f = open('robot.p','wb')
            #pickle.dump(parent , 'fb' )
            #fb.close()
#sensorData = sim.get_sensor_data( sensor_id = P2 ) #collects sensor data
#print(sensorData) #prints sensor data in 0s/1s in a vector
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(x, y, z) #matplotlib graphing
#panel.set_ylim(-1,+2) #limits y-axis
#plt.show()

