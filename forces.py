# -*- coding: utf-8 -*-
class forces():
    def gravity(M,m,r):
        """ 
        calculates the gravitational force felt by two objects
        """
        #G is the gravitational constant
        #M is the mass of object 1
        #m is the mass of object 2
        #r is the distance between the two objects
        G=6.674*(10**11)
        F=((G*M*m)/(r**2))
        return F

    def airrecistance(u,Cd,A,rho):
        """
        calculates the air resisstance felt by an object
        """
        #u is the velocity of the liquid within which the object is moving,
        #Cd is the drag coeficient of the object
        #A is the surface area of the object in question,
        #rho is the density of the liquid
        F=(u**2)*Cd*A*rho*0.5
        return F