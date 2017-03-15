# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:25:07 2017

@author: nilslanglois-cannon
"""

from math import pi, sqrt
import matplotlib.pyplot as plt




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

acceleration = 0
initial_pressure = 10
height = 10
density = 998
volume = Volume(height)
initial_volume = volume
bottle_height = 11
bottle_volume = Volume(bottle_height)
gamma = 1.4
delta = 0.1
bottle_mass = 0
pressure = 10

liq_vel = []
liq_H = []
tt=[]


def velocity_update():
        """
        updates the velocity according to the equations 
        """
        C = 0.5*((Area(0)/Area(height))**2-1)
        D = ((volume-initial_volume)/(bottle_volume-volume))**gamma
        E = bottle_mass*(acceleration+9.81)/density*Area(0)*height
        F=(D*initial_pressure/density) + (acceleration+9.81)*height
        G=C/B(height)
        I=(1+Area(0)/Area(height))/height
        velocity=sqrt(abs((E+F)/(G+I)))
        liq_vel.append(velocity)
        return velocity

def pressure_update():
        """
        updates the pressure using the Pv=k law
        """
        part1 = bottle_volume - initial_volume
        part2 = bottle_volume - volume
        pressure = part1 / part2
        pressure = pressure**gamma
        pressure = pressure * initial_pressure
        
        return pressure

for i in range(5000):      
    #mundane updating of the variables
    velocity = velocity_update()
    #acceleration = self.velocity*delta
    volume_lost = velocity*Area(0)*delta
    volume -= volume_lost
    flowrate = volume_lost * density/delta
    bottle_mass -= volume_lost * density
    height -= delta*velocity*Area(0)/Area(height)
    pressure = pressure_update()
    liq_H.append(height)
    tt.append[i*delta]

plt.subplot(3,1,1)
plt.plot(tt,liq_vel)
plt.title("Liquid Velocity")

plt.subplot(3,1,2)
plt.plot(tt,liq_H)
plt.title("Liquid Height")

plt.show