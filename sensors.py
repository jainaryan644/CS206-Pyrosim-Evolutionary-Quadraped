import pyrosim
import matplotlib.pyplot as plt
sim = pyrosim.Simulator( play_paused = True)
whiteObject = sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 )
redObject = sim.send_cylinder( x=0 , y=0.5 , z=1.1, r=1, g=0, b=0, r1=0 , r2=1 , r3=0 )
joint = sim.send_hinge_joint( first_body_id = whiteObject , second_body_id = redObject, x = 0, y = 0, z = 1.1, n1 = -1 , n2 = 0 , n3 = 0, lo=-3.14159/2 , hi=3.14159/2)
T0 = sim.send_touch_sensor( body_id = whiteObject )
T1 = sim.send_touch_sensor( body_id = redObject )
P2 = sim.send_proprioceptive_sensor( joint_id = joint )
R3 = sim.send_ray_sensor( body_id = redObject , x = 0.25 , y = 0.5, z = 1.1 , r1 = 0 , r2 = 0, r3 = -1)
sim.start()
sim.wait_to_finish()
sensorData = sim.get_sensor_data( sensor_id = R3 )
print(sensorData)
f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
#panel.set_ylim(-1,+2)
plt.show()



















































































