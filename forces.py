# -*- coding: utf-8 -*-

class Forces:
    """
    Class to calculate the forces acting on an object
    """
    def gravity(M, m, r):
        """ 
        Calculates the gravitational force felt by two objects, where:
        G is the gravitational constant,
        M is the mass of the first object,
        m is the mass of the second object, and
        r is the distance between the two objects. 
        """
        G = 6.674 * (10**11)
        F = (G*M*m) / (r**2)
        
        return F

    def air_resistance(u, Cd, A, rho):
        """
        Calculates the air resistance felt by an object, where:
        u is the velocity of the liquid within which the object is moving,
        Cd is the drag coefficient of the object,
        A is the surface area of the object, and
        rho is the density of the liquid.
        """
        F = (u**2) * Cd * A * rho * 0.5
        
        return F
