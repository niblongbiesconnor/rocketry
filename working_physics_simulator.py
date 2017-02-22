#my imported 
from math import pi 
import matplotlib.pyplot as plt
#x and y values DONT alter 
pos=[]               
tt=[]                  
#these are varibales that change automatically they should all equal 0 apart from delta 
rec = 0 
delta = 0.001def r(x):    
r = 0.1    
  if x == 0:        
    r = 0    return r        def A(x):    r=pi*x**2    return r#rocket characteristics class rocket():     """     the rocket class contains most of the rocket based variables needs to be updated     """     def __init__(self):          self.radius = 0.1           self.mbottle = 0.1         self.Force = 0         self.acceleration = 0          self.velocity = 0         self.bottle_length=10         self.height = 0        def B(water):        for i in range(water.height/delta):            water.volume+=(A(i*delta)*delta)                    def update(self):             rhino.mass=self.mbottle+liquid.volume                if liquid.volume > 0:             self.F+=abs(liquid.flowrate*liquid.v)         self.acceleration=(self.Force/self.mass)-9.81         self.velocity+=self.acceleration*delta        self.height+=self.velocity*delta                 pos.append(self.height)        tt.append(delta*rec)class liquid:     """    contains all the liquid variables     """    def __init__(self):       self.acceleration = 0       self.velocity = 0       self.volume = 22       self.flowrate = 0       self.pressure = 1000       #the height of the water in the vessel       self.height = 10        def update(self):        #using the finite difference method        self.acceleration=(self.pressure/self.volume)-9.81         self.velocity+=self.acceleration*delta                if self.volume > 0:            volume_lost=abs(self.velocity*pi*(rhino.radius**2)*delta)             self.volume-=volume_lost            self.flowrate=volume_lost/deltawater=liquid()rhino=rocket()rhino.a=-1000*water.height*A(0)/rhino.massrhino.a=rhino.a*liquid.pressure*A(0)/rhino.mass while (rec < 1000):    rec+=1    liquid.update()    rhino.update() plt.plot(tt,pos)plt.show()
