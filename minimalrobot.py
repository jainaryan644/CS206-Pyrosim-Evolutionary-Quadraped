import pyrosim
class ROBOT:
    def __init__(self,sim, wts):
        whiteObject = sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 ) # white cylinder
        redObject = sim.send_cylinder( x=0 , y=0.5 , z=1.1, r=1, g=0, b=0, r1=0 , r2=1 , r3=0 ) # red cylinder
        joint = sim.send_hinge_joint( first_body_id = whiteObject , second_body_id = redObject, x = 0, y = 0, z = 1.1, n1 = -1 , n2 = 0 , n3 = 0, lo=-3.14159/2 , hi=3.14159/2)
        T0 = sim.send_touch_sensor( body_id = whiteObject ) #touch sensor 1
        T1 = sim.send_touch_sensor( body_id = redObject ) # touch sensor 2
        P2 = sim.send_proprioceptive_sensor( joint_id = joint ) # proprioceptive sensor
        R3 = sim.send_ray_sensor( body_id = redObject , x = 0.25 , y = 0.5, z = 1.1 , r1 = 0 , r2 = 0, r3 = -1) #ray sensor
        SN1 = sim.send_sensor_neuron( sensor_id = T0 )  # sensor neuron -- sensor 1
        SN2 = sim.send_sensor_neuron( sensor_id = T1 ) # sensor neuron -- sensor 2
        SN3 = sim.send_sensor_neuron( sensor_id = P2 ) # sensor neuron -- sensor 3
        SN4 = sim.send_sensor_neuron( sensor_id = R3 ) # sensor neuron -- sensor 4 
        sensorNeurons = {}
        sensorNeurons[0]= SN1
        sensorNeurons[1]= SN2
        sensorNeurons[2]= SN3
        sensorNeurons[3]= SN4
        MN2 = sim.send_motor_neuron( joint_id = joint ) #motorized joint with neuron 
        motorNeurons = {}
        motorNeurons[0]= MN2
        for s in sensorNeurons:
            for m in motorNeurons:
                sim.send_synapse(source_neuron_id = sensorNeurons[s] , target_neuron_id = motorNeurons[m] , weight = wts[s] ) #connects SN1 & MN2
        self.P4 = sim.send_position_sensor( body_id = redObject ) # position sensor  
        #sim.send_synapse(source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 ) #connects SNO & MN2
         



















