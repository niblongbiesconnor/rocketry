# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:09:49 2017
@author: user
"""
#my imported 
from math import pi, sqrt, log
import matplotlib.pyplot as plt

#x and y values DONT alter used for plotting
acc = []
vel = []
pos = []               
tt = []
liq_vel = []           
liq_H = []
  
#these are varibales that change automatically they should all equal 0 apart from delta 
delta = 0.01
gamma = 1.4

def Radius(height):
    radius = 0.1
    #our current assumption is a cylinder with a hole of radius 0.01m in the base
    if height == 0:
        radius = 0.01
    return radius

def Area(height):
    area = pi*Radius(height)**2
    return area

def Volume(height):
    volume=0
    for i in range(int(height/delta)):
        volume += (Area(i * delta) * delta)
    return volume

#rocket characteristics 
class rocket(): 
    """ 
    the rocket  contains most of the rocket based variables needs to be updated 
    """ 
    def __init__(self):
        """
        innitialisations of the rockets variables 
        """
        #the bottles characterisitics and other constants
        self.mbottle = 0.048
        self.bottle_length = 4
        self.volume = Volume(self.bottle_length)
       
        
        #the rockets variables
        self.mass = self.mbottle + (water.volume*water.density)
        self.initial_mass = self.mass
        self.Force = 0
        self.velocity = 0
        self.acceleration = -9.81  #self.initial_acceleration()
        self.height = 0
    
    def initial_acceleration(self):
        def B(height):
            y = 0
            for i in range(int(round(height/delta))):
                y += Area(0) / (Area(i*delta)*delta)
            return y
        
        part1 = water.initial_pressure*Area(0)/rhino.mass
        part2 = B(water.height)/water.height
        part3 = water.density*water.height*Area(0)/rhino.mass
        acceleration = 9.81 + part1/(part2-part3)
        
        return(acceleration)
   
    def water_update(self):
        """
        updates the rockets position if there is still water within the rocket
        """
        
        rhino.mass = rhino.mbottle + (water.volume * water.density)
        #self.acceleration = water.velocity * log(self.initial_mass / self.mbottle)
        if self.mass<self.mbottle:
            self.mass = self.mbottle
        self.acceleration = (water.volume_lost*water.density)*water.velocity/(rhino.mass*delta)
        self.acceleration -= 9.81
        self.velocity += self.acceleration * delta
        self.height += self.velocity * delta
        
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
       self.pressure = 1296000
       self.initial_pressure = self.pressure
       self.density = 998
       self.height = 1.3
       self.initial_height = self.height
       self.volume = Volume(self.height)
       self.initial_volume = self.volume
       self.initial_temp = 293
       self.volume_lost = 0

        
    def water_update(self):

        def velocity_update():
            """
            updates the velocity according to the equations 
            """
            part1 = 2 * (water.pressure + (water.density * water.height * (rhino.acceleration + 9.81)))
            part2 = water.density * (1 - (Area(0) / Area(water.height)) **2)
            velocity = sqrt(part1/part2)

            return velocity
        
        def pressure_update():
            """
            updates the pressure using the Pv=k law
            """
            part1 = rhino.volume - self.initial_volume
            part2 = rhino.volume - self.volume
            pressure = part1 / part2
            pressure = pressure**gamma
            pressure = pressure * self.initial_pressure
            
            return pressure
          
        #mundane updating of the variables
        self.velocity = velocity_update()
        height_lost = self.velocity*delta
        self.volume_lost = height_lost*Area(0)
        self.volume -= self.volume_lost
        #self.height = inv_volume(self.volume)
        
        self.pressure = pressure_update()
        liq_vel.append(self.velocity)
        liq_H.append(self.height)
        
    def final_temperature(self):
        part1 = 1-(water.initial_volume/rhino.volume)
        part2 = part1 **(self.gamma-1)
        temperature = self.initial_temp * part2
        return temperature
        
class gas():
    
    def __init__(self):
        self.gamma = 1.4
        self.Rm = 8.314510/0.028964
        self.temperature = 217
        self.pressure = water.pressure
        self.initial_pressure = self.pressure
        self.initial_temp = water.final_temperature()
        self.t = 0
        self.beta = 1.03 + 0.021*self.gamma
        self.initial_velocity = sqrt(self.gamma * self.Rm * self.initial_temp)
        self.time_k = self.time_constant()
        self.total_t = self.total_time()
        
    def total_time(self):
        part1 = self.initial_pressure/(self.beta*0.01)
        part2 = (self.gamma - 1) / (2*self.gamma)
        time = self.time_k*(part1**part2 - 1)

        return time

    def pressure_update(self):
        """
        finds the pressure
        """
        part1 = 1 + (self.t / self.time_k)
        part2 = (2 * self.gamma) / (1 - self.gamma)
        self.pressure = self.initial_pressure * part1 ** part2
        self.t += delta

    def acceleration(self):
        """
        finds the acceleration
        """
        self.pressure_update()
        part1 =  2 * self.pressure * Area(0)
        part2 = 2 / (1 + self.gamma)
        part3 = 1 / (self.gamma - 1)
        thrust = part1 * (part2 ** part3)
        acceleration = (thrust/rhino.mass) -9.81
                       
        return acceleration
    
    def time_constant(self):
        """
        finds the time constant
        """
        part1 = rhino.volume/(Area(0)*self.initial_velocity)
        part2 = 2/(self.gamma-1)
        part3 = (self.gamma+1) / (2*(self.gamma-1))
        part4 = ((self.gamma + 1)/2)**part3
        tau = part1*part2*part4
        
        return tau
    
    
#initialisation of the classes
water = liquid()
rhino = rocket()
air = gas()
#the main part of the program
rec=0

def gravity_update():
    distance = 384432*10^3
    distance+=rhino.height
    acceleration = 3.9857606e+14/(distance**2)
    return acceleration

def water_phase():
    global rec
    while water.volume>0.0001:
        if (rec%1000) == 0:
            gravity_update()
        water.water_update()
        rhino.water_update()
        rec+=1
        tt.append(rec*delta)

def gas_phase():
    global rec
    while air.t<air.total_t:
        rhino.gas_update()
        rec+=1
        liq_vel.append(0)
        liq_H.append(0)
        tt.append(rec*delta)

def fall_phase():
    global rec
    while rhino.height>0:
        rhino.fall()
        rec+=1
        liq_vel.append(0)
        liq_H.append(0)
        tt.append(rec*delta)

    
def plotting():
    plt.subplot(5,1,1)
    plt.plot(tt,acc)
    plt.title("Acceleration")
        
    plt.subplot(5,1,3)
    plt.plot(tt,vel)
    plt.title("Velocity")
        
    plt.subplot(5,1,5)
    plt.plot(tt,pos)
    plt.title("Altitude")
    
    """
    plt.subplot(9,1,7)
    plt.plot(tt,liq_vel)
    plt.title("Liquid Velocity")
    
    plt.subplot(9,1,9)
    plt.plot(tt,liq_H)
    plt.title("Liquid Height")
    plt.show
    """
    
water_phase()
gas_phase
fall_phase()
plotting()
    
#if __name__ == "__main__": 
#    main()