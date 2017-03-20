# -*- coding: utf-8 -*-

"""
Calculates the rocket's total work done
"""
from math import pi 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
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


# Ratio of specific heat transfer
gamma=1.4
# List of all times
filling_fraction_list=[]
# Function of all times
workdone_list=[]
# Pressure of air in bottle at the moment about 3 atmospheres
P=4*(10**5)
Patm=0.001
height=0.3
V= Volume(height)
#density of the liquid
rho=998

#The total mass of the rocket when empty
mass_rocket=10
    
def WDgasblast(f):
    """
    calculates the work done in the gas blast
    """
    part1=(P*V)/(-gamma+1)
    try:
        part2 = (1-f)**(-gamma+1)
    except:
        part2 = 0.00001
    part3=(P/Patm)**(1/gamma-1)
    part4=(part2*part3)-1
    workdone=part1*part4
    return workdone
    
def workdone(f):
    """
    Calculates work done for various values of f
    """
    top = P * V*(((1-f)**gamma)-(1-f))
    bottom = (-gamma+1)
    workdone = top / bottom
    workdone+=(WDgasblast(f))
    return workdone

def WDweightratio(f):
    """
    Calculate the work done per kilogram of mass
    """
    
    workd = workdone(f) 
    mass = (f * V * rho) + mass_rocket
    WMR = workd / mass
    return WMR

def findtotalWD():
    """
    Calculate the work done
    """
    #Calculate for variouis values of filling fractions
    for i in range(1000): 
        f = i*0.001 
        x = workdone(f) 
        filling_fraction_list.append(f) 
        workdone_list.append(x) 
    return filling_fraction_list, workdone_list

def findtotalWDMR():
    """
    Calculate work done mass ratio
    """
    # Calculate for various values of filling fractions
    filling_fraction_list=[]
    workdone_list = []
    for i in range(1000): 
        f = i*0.001 
        x = WDweightratio(f) 
        filling_fraction_list.append(f) 
        workdone_list.append(x) 
    return filling_fraction_list, workdone_list

def findtotaldensity_WDMR_FF():
    """
    finds the values for the 3d plot of the workdone-mass-ratio, Density, Filling Fraction
    """
    X = []
    Y = []
    Z = []
    global rho
    
    for i in range(1000):
        den_list=[]
        
        rho = i
        x , y = findtotalWDMR()
        X.append(x[i])
        Y.append(y[i])
        for j in range(len(x)):
            den_list.append(i)
        Z.append(den_list)
    
    X=np.array(X)
    Y=np.array(Y)
    Z=np.array(Z, float)

    return(X , Z , Y)

def findtotalden_WDMR():
    global rho
    den_list = []
    workdone_list = []
    
    for i in range(1,1000):
        rho = i
        x , y = findtotalWDMR()
        workdone_list.append(max(y))
        
    for i in range(len(workdone_list)):
        den_list.append(i)
        
    return den_list, workdone_list

def findtotalheight_density_WDMR():
    height_list = []
    X = []
    Y = []
    Z = []
    global height
    global V
    for i in range(1000):
        height = i*0.1
        V=Volume(height)
        x,y = findtotalden_WDMR()
        X.append(x)
        Y.append(y)
        for j in range(len(x)):
            height_list.append(i)
        Z.append(height_list)
    X=np.array(X)
    Y=np.array(Y)
    Z=np.array(Z, float)
    return X, Y, Z

def findtotalheight_WDMR():
    height_list = []
    workdone_list = []
    global height
    global V

    for i in range(10000):
        height = i*0.001
        V = Volume(height)
        x,y = findtotalWDMR()
        height_list.append(height)
        workdone_list.append(max(y))
    
    return (height_list , workdone_list)

def findtotal_height_WDMR_FF():
    height_list = []
    X = []
    Y = []
    Z = []
    global height
    global V
    for i in range(1000):
        height = i*0.1
        V=Volume(height)
        x,y = findtotalWDMR()
        X.append(x)
        Y.append(y)
        for j in range(len(x)):
            height_list.append(i)
        Z.append(height_list)
    X=np.array(X)
    Y=np.array(Y)
    Z=np.array(Z, float)
    return X, Y, Z
        
    

def graph_height_den_WDMR():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z= findtotalheight_density_WDMR()
    ax.plot_surface(X , Y , Z)
    ax.set_xlabel('Height')
    ax.set_ylabel('Density')
    ax.set_zlabel("Workdone per Unit Mass")
    plt.title("Workdone per Unit Mass Against Height Against Density")

def graph_height_WDMR_FF():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z= findtotal_height_WDMR_FF()
    ax.plot_surface(X , Y , Z)
    ax.set_xlabel('Height')
    ax.set_ylabel('Filling Fraction')
    ax.set_zlabel("Workdone per Unit Mass")
    plt.title("Workdone per Unit Mass Against Height Against Density")

def graph_height_WDMR():
    x , y = findtotalheight_WDMR()
    plt.plot(x,y)
    plt.ylabel("Work Done per Unit Mass")
    plt.xlabel("Height")
    plt.title("Work Done per Unit Mass Against Height")
    plt.show()

def graph_den_WDMR_FF():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z= findtotaldensity_WDMR_FF()
    ax.plot_surface(X , Y , Z)
    ax.set_xlabel('Filling Fraction')
    ax.set_ylabel('Density')
    ax.set_zlabel("Workdone per Unit Mass")
    plt.title("Workdone per Unit Mass Against Filling Fraction Against Density")

def graph_den_WDMR():
    x , y = findtotalden_WDMR()
    plt.plot(x,y)
    plt.ylabel("Work Done per Unit Mass")
    plt.xlabel("Density")
    plt.title("Work Done per Unit Mass Against Density")
    plt.show()
    
def graph_WDMR_FF():
    x,y=findtotalWDMR()
    plt.plot(x,y)
    plt.ylabel("Work Done per Unit Mass")
    plt.xlabel("Filling Fraction")
    plt.title("Work Done per Unit Mass Against Filling Fraction")
    plt.show()

def graph_WD_FF():
    x,y=findtotalWD()
    plt.plot(x,y)
    plt.ylabel("Work Done (Joules)")
    plt.xlabel("Filling Fraction")
    plt.title("Work Done Against Filling Fraction")
    plt.show()
     
graph_height_WDMR_FF()