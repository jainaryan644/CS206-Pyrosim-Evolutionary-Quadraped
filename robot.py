import pyrosim
import constants as c
import math
import random

class ROBOT:
    def __init__(self,sim, wts):
        
        self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        self.O1 = sim.send_cylinder(x=0 ,y=c.L, z=c.L + c.R, length= c.L, radius = c.R, r1=0, r2=1, r3=0, r=1, g=0, b=0)
        self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L+c.R, length=c.L, radius = c.R, r1=1, r2=0, r3=0, r=0, g=1, b=0)
        self.O3 = sim.send_cylinder(x=0, y=-c.L, z = c.L + c.R, length=c.L, radius=c.R, r1=0, r2=-1, r3=0, r=0, g=0, b=1)
        self.O4 = sim.send_cylinder(x=-c.L, y=0, z = c.L + c.R, length=c.L, radius=c.R, r1=-1, r2=0, r3=0, r=1, g=0, b=1)
        self.O5 = sim.send_cylinder(x=0, y=1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=0)
        self.O6 = sim.send_cylinder(x=1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=1, b=0)
        self.O7 = sim.send_cylinder(x=0, y=-1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=0, b=1)
        self.O8 = sim.send_cylinder(x=-1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=1)

        self.O={} #Object dictionary
        self.O[0]=self.O0
        self.O[1]=self.O1
        self.O[2]=self.O2
        self.O[3]=self.O3
        self.O[4]=self.O4
        self.O[5]=self.O5
        self.O[6]=self.O6
        self.O[7]=self.O7
        self.O[8]=self.O8

        
        #whiteObject = sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 ) # white cylinder
        #redObject = sim.send_cylinder( x=0 , y=0.5 , z=1.1, r=1, g=0, b=0, r1=0 , r2=1 , r3=0 ) # red cylinder
        self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1,x=0, y=c.L/2, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5,x=0, y=1.5* c.L, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2,x=c.L/2, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6,x=1.5 * c.L, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3,x=0, y=-c.L/2, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7,x=0, y=-1.5*c.L, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4,x=-c.L/2, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8,x=-1.5*c.L, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)

        self.J={} #joint dictionary
        self.J[0]=self.J0
        self.J[1]=self.J1
        self.J[2]=self.J2
        self.J[3]=self.J3
        self.J[4]=self.J4
        self.J[5]=self.J5
        self.J[6]=self.J6
        self.J[7]=self.J7

        #add_sensors
        self.T0 = sim.send_touch_sensor( body_id = self.O5 ) #red leg sensor
        self.T1 = sim.send_touch_sensor( body_id = self.O6 ) # green leg sensor
        self.T2 = sim.send_touch_sensor( body_id = self.O7 ) # blue leg sensor
        self.T3 = sim.send_touch_sensor( body_id = self.O8 ) # pink leg sensor
        self.L4 = sim.send_light_sensor( body_id = self.O0 ) # light sensor

        self.S={} # touch sensor dictionary
        self.S[0]=self.T0
        self.S[1]=self.T1
        self.S[2]=self.T2
        self.S[3]=self.T3
        self.S[4]=self.L4


        #send_neurons
        self.SN = {} # sensor neuron dictionary
        self.MN = {} # motor neuron dictionary

        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s]) # adds all of the sensor neurons from the touch sensors
        
        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau= 0.3) # stores the joints in the motor neurons
        
        
        #for j in self.SN:
        #   firstMN = min( self.MN , key=self.MN.get )
        #       self.wire[j]=sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[firstMN], weight=wts[j]) # joins the motor neurons and sensor neurons
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse( source_neuron_id = self.SN[j] , target_neuron_id = self.MN[i], weight = wts[j,i] )
                
        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN
       # P2 = sim.send_proprioceptive_sensor( joint_id = joint ) # proprioceptive sensor
       # R3 = sim.send_ray_sensor( body_id = redObject , x = 0.25 , y = 0.5, z = 1.1 , r1 = 0 , r2 = 0, r3 = -1) #ray sensor
        
       # SN1 = sim.send_sensor_neuron( sensor_id = T0 )  # sensor neuron -- sensor 1
        #SN2 = sim.send_sensor_neuron( sensor_id = T1 ) # sensor neuron -- sensor 2
       # SN3 = sim.send_sensor_neuron( sensor_id = P2 ) # sensor neuron -- sensor 3
       # SN4 = sim.send_sensor_neuron( sensor_id = R3 ) # sensor neuron -- sensor 4 
       # sensorNeurons = {}

       # sensorNeurons[0]= SN1
       # sensorNeurons[1]= SN2
       # sensorNeurons[2]= SN3
       # sensorNeurons[3]= SN4
       # MN2 = sim.send_motor_neuron( joint_id = joint ) #motorized joint with neuron 
        #motorNeurons = {}
       # motorNeurons[0]= MN2
       # for s in sensorNeurons:
       #     for m in motorNeurons:
      #          
        #sim.send_synapse(source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 ) #connects SNO & MN2
         


