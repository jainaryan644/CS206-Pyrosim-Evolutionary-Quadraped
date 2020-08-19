import pyrosim
import random
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
for i in range(0,2):
    #x = sim.get_sensor_data( sensor_id = robot.P4 , svi = 0 )
    #y = sim.get_sensor_data( sensor_id = robot.P4 , svi = 0 )
   # 
    #print(z[-1])
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)
#sensorData = sim.get_sensor_data( sensor_id = P2 ) #collects sensor data
#print(sensorData) #prints sensor data in 0s/1s in a vector
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(x, y, z) #matplotlib graphing
#panel.set_ylim(-1,+2) #limits y-axis
#plt.show()

