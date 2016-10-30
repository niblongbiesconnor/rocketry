#my imported
from math import pi
from pylab import plot,show

#x and y values DONT alter
pos=[]              
tt=[]               



#constants change only for accuracy
class constants():
    """
    defines all of the constants used
    """
    def __init__(self):
        self.gconstant=-9.81
        self.denair=0.0001
        self.denliq=1
        self.CelsiusToKelvin=274.150


#these are varibales that change automatically they should all equal 0 apart from delta
rec=0
delta=0.001

#rocket characteristics
class rocket():
    """
    the rocket class contains most of the rocket based variables needs to be updated
    """
    def __init__(self):
        #the radius of the bottle
        self.r=0.1
        #the mass of the empty bottle
        self.mbottle=0.1
        #the drag coefficient
        self.Cd=1
        #the surface area of the front cone
        self.Area=0.0314
        #the force
        self.F=0
        #the acceleration
        self.a=0
        #the velocity
        self.v=0
        #the position
        self.y=0

class liq:
    """
    contains all the liquid variables
    """
    def __init__(self):
        #the force
        self.F=0
        #the acceleration
        self.a=0
        #the velocity
        self.v=0
        #the volume of water
        self.volume=1

    def mass(self):
        """
        calculates the mass of the liquid
        """
        mass=self.volume*constant.denliq
        return mass
liquid=liq()
rhino=rocket()
constant=constants()

def pressureliq():
    F=10
    return F

def AirRec(v,denair,FrontArea,Cd):
    F=(v**2)*0.5*FrontArea*denair*Cd
    if v>0:
        F=F*-1
    return F






#the big one

while (rec<100):
    rec+=1

    #the liquids frame of reference
    #the force on the liquid
    liquid.F=pressureliq()
    #the acceleration felt is equal to the force plus the gravity
    liquid.a=(liquid.F/liquid.mass())-9.81
    #the velocity is equal to the integral of time over this period
    liquid.v+=liquid.a*delta
    volume_lost=abs(liquid.v*pi*(rhino.r**2)*delta)
    liquid.volume-=volume_lost
    flowrate=(volume_lost*constant.denliq)/delta


    #the rockets frame of reference
    mass=mbottle+liquid.volume/denliq
    rhino.F=AirRec(rhino.v,constant.denair,rhino.Area,rhino.Cd)
    if liquid.volume>0:
        rhino.F+=abs(flowrate*liquid.v)
    rhino.a=(rhino.F/mass)-9.81
    rhino.v+=rhino.a*delta
    rhino.y+=rhino.v*delta
    pos.append(rhino.y)
    tt.append(delta*rec)

plot(tt,pos)
show()

    
