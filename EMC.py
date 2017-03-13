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
rec = 0 
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
    the rocket class contains most of the rocket based variables needs to be updated 
    """ 
    def __init__(self):
        #the bottles characterisitics and other constants
        self.mbottle = 0.1
        self.bottle_length=11
        self.volume=Volume(self.bottle_length)
        self.initial_mass = self.mbottle+water.volume*water.density
        
        
        #the rockets variables
        self.mass = self.mbottle+water.volume*1000 
        self.Force = 0
        self.velocity = 0
        self.acceleration = self.initial_a()
        self.height=0
    
    def tube_update():
        part1=2*water.initial_pressure*water.initial_volume/(mass*(1-gamma)
        part2=(self.height*Area(rhino.tube_radius)/water.initial_volume+1)**(1-gamma)-1
        part3=2*self.height*(Area(rhino.tube_radius))/
        self.velocity=sqrt(part1*part2-part3)
    
    def water_update():
    
        def initial_a(self):
            acceleration=-water.density*water.height*Area(0)/self.mass                                    
            acceleration+=B(water.initial_height)/water.initial_height
            acceleration=acceleration*(water.pressure*Area(0)/self.mass)
            print (acceleration)
            acceleration-=9.81
            return acceleration
        
        def update(self):     
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
            tt.append(delta*rec)




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
    
    
        
    def tube_update(self):
        self.velocity = self.velocity_update()
        self.acceleration = self.velocity*delta
        volume_lost = self.velocity*Area(0)*delta
        self.volume -= volume_lost
        self.flowrate = volume_lost*self.density/delta
        rhino.mass -= volume_lost*self.density
        
    def water_update(self):
        
        def velocity_update(self):
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
        
        def pressure_update(self):
            part1 = rhino.volume - water.initial_volume
            part2 = rhino.volume - water.volume
            pressure = part1 / part2
            pressure = pressure**gamma
            pressure = pressure * water.initial_pressure
            
            return pressure
            
        self.velocity = self.velocity_update()
        self.acceleration = self.velocity*delta
        volume_lost = self.velocity*Area(0)*delta
        self.volume -= volume_lost
        self.flowrate = volume_lost*self.density/delta
        rhino.mass -= volume_lost*self.density
        self.height -= delta*self.velocity*Area(0)/Area(self.height)
        self.pressure = self.pressure_update()
        liq_H.append(self.height)
            
    def air_update(self):
        return self.acceleration
    
    def space_fall(self):
        return self.accelereation
    
    def atmosphere_fall(self):
        return self.acceleration
        
def tube()
    while height<tube.height:
            water.tube_update
            rhino.update()
            
def water_blast(self):
    while water.height>0:
        water.water_update()
        rhino.update()
    return self.acceleration

def air_blast(self):
    while water.air_density>0:
        water.air_update>0
    return self.acceleration

def space_fall(self):
    return self.accelereation

def atmosphere_fall(self):
    return self.acceleration



    


water=liquid()
rhino=rocket()

while (rec < 10):
    rec+=1
    
    if water.volume >= 0:
        water.update()
    else:
        liq_vel.append(0)
        liq_H.append(0)
        rhino.update()
        break
    rhino.update()
    
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