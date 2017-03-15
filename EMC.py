#my imported 
from math import pi, sqrt, log
import matplotlib.pyplot as plt

#x and y values DONT alter used for plotting
acc=[]
vel=[]
pos=[]               
tt=[]
liq_vel=[]           
liq_H=[]
  
#these are varibales that change automatically they should all equal 0 apart from delta 
delta = 0.1
gamma=1.4

def Radius(height):
    radius = 0.1
    #our current assumption is a cylinder with a hole of radius 0.01m in the base
    if height == 0:
        radius = 0.01
        
    return radius

def Area(height):
    area=pi*Radius(height)**2
    return area

def Volume(height):
    volume=0
    for i in range(int(height/delta)):
        volume+=(Area(i*delta)*delta)
    return volume

def B(height):
    y=0
    for i in range(int(round(height/delta))):
        y+=Area(0)/(Area(i*delta)*delta)
    return y



    
#rocket characteristics 
class rocket(): 
    """ 
    the rocket  contains most of the rocket based variables needs to be updated 
    """ 
    def __init__(self):
        #the bottles characterisitics and other constants
        self.mbottle = 0.1
        self.bottle_length=11
        self.volume=Volume(self.bottle_length)
       
        
        
        #the rockets variables
        self.mass = self.mbottle+water.volume*water.density
        self.initial_mass =  self.mass
        self.Force = 0
        self.velocity = 0
        self.acceleration = -9.81
        self.height = 0
        
    def water_update(self):
        rhino.mass=rhino.mbottle+water.volume*water.density
        self.acceleration=water.velocity*log(self.initial_mass/(self.mbottle)*delta)
        self.velocity+=self.acceleration*delta
        self.height+=self.velocity*delta
        
        if self.height <= 0:
            self.height = 0
            self.velocity = 0
            self.acceleration = 0
        acc.append(self.acceleration)
        vel.append(self.velocity)
        pos.append(self.height)
        
    
    def fall(self):
        self.acceleration=-9.81
        self.velocity+=self.acceleration*delta
        self.height+=self.velocity*delta
        
        if self.height <= 0:
                self.height = 0
                self.velocity = 0
                self.acceleration = 0
                
        acc.append(self.acceleration)
        vel.append(self.velocity)
        pos.append(self.height)
        




class liquid: 
    """
    contains all the liquid variables
    """
    def __init__(self):
       self.gamma = 1.4
       self.acceleration = 0
       self.velocity = 0
       self.flowrate = 0
       self.pressure = 10
       self.initial_pressure = self.pressure
       self.density = 998
       self.height = 10
       self.initial_height = self.height
       self.volume = Volume(self.height)
       self.initial_volume = self.volume

        
    def water_update(self):
        
        def velocity_update():
            """
            updates the velocity according to the equations 
            """
            C=0.5*((Area(0)/Area(water.height))**2-1)
            D=((rhino.volume-water.initial_volume)/(rhino.volume-water.volume))**gamma
            E=rhino.mass*(rhino.acceleration+9.81)/water.density*Area(0)*water.height
            F=(D*water.initial_pressure/water.density) + (rhino.acceleration+9.81)*water.height
            G=C/B(water.height)
            I=(1+Area(0)/Area(water.height))/water.height
            velocity=sqrt(abs((E+F)/(G+I)))
            liq_vel.append(velocity)
            return velocity
        
        def pressure_update():
            """
            updates the pressure using the Pv=k law
            """
            part1 = rhino.volume - water.initial_volume
            part2 = rhino.volume - water.volume
            pressure = part1 / part2
            pressure = pressure**gamma
            pressure = pressure * water.initial_pressure
            
            return pressure
          
        #mundane updating of the variables
        self.velocity = velocity_update()
        self.acceleration = self.velocity*delta
        volume_lost = self.velocity*Area(0)*delta
        self.volume -= volume_lost
        self.flowrate = volume_lost*self.density/delta
        rhino.mass -= volume_lost*self.density
        self.height -= delta*self.velocity*Area(0)/Area(self.height)
        self.pressure = pressure_update()
        liq_H.append(self.height)

#initialisation of the classes
water=liquid()
rhino=rocket()



#the main part of the program
rec=0
while water.height>0.1:
    water.water_update()
    rhino.water_update()
    rec+=1
    tt.append(rec*delta)

while rhino.height>0:
    rhino.fall()
    rec+=1
    liq_vel.append(0)
    liq_H.append(0)
    tt.append(rec*delta)

    



    
def plotting():
    plt.subplot(9,1,1)
    plt.plot(tt,acc)
    plt.title("Acceleration")
        
    plt.subplot(9,1,3)
    plt.plot(tt,vel)
    plt.title("Velocity")
        
    plt.subplot(9,1,5)
    plt.plot(tt,pos)
    plt.title("Altitude")
    
    plt.subplot(9,1,7)
    plt.plot(tt,liq_vel)
    plt.title("Liquid Velocity")
    
    plt.subplot(9,1,9)
    plt.plot(tt,liq_H)
    plt.title("Liquid Height")
    
    plt.show

plotting()