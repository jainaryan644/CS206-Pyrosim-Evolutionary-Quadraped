import pyrosim
import random
import matplotlib.pyplot as plt
from robot import ROBOT
for i in range(0,8):
    sim = pyrosim.Simulator( play_paused = True, eval_time =500) #starts the simulation paused
    robot = ROBOT( sim, random.random()*2 - 1 )
    sim.start()
    sim.wait_to_finish()
#sensorData = sim.get_sensor_data( sensor_id = P2 ) #collects sensor data
#print(sensorData) #prints sensor data in 0s/1s in a vector
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData) #matplotlib graphing
#panel.set_ylim(-1,+2) #limits y-axis
#plt.show()















