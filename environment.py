import constants as c

class environment: 
    def __init__ (self, e):
        self.ID = e
        self.length = c.L
        self.w = c.L 
        self.h = c.L 

        

        if( self.ID == 0):
            self.Place_Light_Source_To_The_Front()
            
        if( self.ID == 1 ):
            self.Place_Light_Source_To_The_Right()
           
        if( self.ID == 2):
            self.Place_Light_Source_To_The_Back()
            
        if( self.ID == 3 ):
            self.Place_Light_Source_To_The_Left()
            
        #print('length:', self.length, ' width:', self.w, ' height:', self.h, ' self.x:', self.x, ' self.y:', self.y,' self.z:', self.z)

    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = c.L *10
        self.z = 0
    
    def Place_Light_Source_To_The_Right(self):
        self.x = c.L * 10
        self.y = 0
        self.z = 0

    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = c.L  * -10
        self.z = 0

    def Place_Light_Source_To_The_Left(self):
        self.x= c.L  * -10
        self.y = 0
        self.z = 0
        
    def Send_To(self,sim):

        lightSource = sim.send_box(x= self.x, y=self.y, z=self.z, length=self.length, width=self.w, height=self.h)      
        sim.send_light_source( body_id = lightSource )

    

        