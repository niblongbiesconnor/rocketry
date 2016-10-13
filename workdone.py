# -*- coding: utf-8 -*-

"""
Calculates the rocket's total work done
"""

import matplotlib.pyplot as plt

class WDCalc:
    """
    Class to calculate total work done for a specific rocket
    """
    def __init__(self):
        """
        Set local variables
        """
        # Ratio of specific heat transfer
        self.gamma=1.4
        # List of all times
        self.filling_fraction_list=[]
        # Function of all times
        self.workdone_list=[]
        # Pressure of air in bottle
        self.P=4*(10**5)
        # Volume of bottle (litres)
        self.V=2*(10**-3) 
        # Density of liquid
        # Currently water
        self.rho=1
        #The total mass of the rocket when empty
        self.mass_rocket=1
        
    def workdone(self, f):
        """
        Calculates work done for various values of f
        """
        # *10**-3 so as to convert units from litres to cubic metres
        top = self.P * self.V * (10**-3)
        bottom = (-self.gamma+1) * ((1-f)**self.gamma)-(1-f)
        workdone = top / bottom
        return workdone 
    
    def WDweightratio(self,f):
        """
        Calculate the work done per kilogram of mass
        """
        workdone = self.workdone(f)
        mass = (f * self.V * (10**-3) * self.rho) + self.mass_rocket
        WMR = workdone / mass
        return WMR
    
    def findtotalWD(self):
        """
        Calculate the work done
        """
        #Calculate for variouis values of filling fractions
        for i in range(1,1001): 
            f = i*0.001 
            x = self.workdone(f) 
            self.filling_fraction_list.append(f) 
            self.workdone_list.append(x) 
            return self.filling_fraction_list, self.workdone_list
    
    def findtotalWDMR(self):
        """
        Calculate work done mass ratio
        """
        # Calculate for various values of filling fractions
        for i in range(1,1001): 
            f = i*0.001 
            x = self.WDweightratio(f) 
            self.filling_fraction_list.append(f) 
            self.workdone_list.append(x) 
            return self.filling_fraction_list, self.workdone_list
    
    def graph_WDMR_FF(self):
        x,y=self.findtotalWDMR()
        plt.plot(x,y)
        plt.ylabel("Work Done per Unit Mass (Joules per Kilogram)")
        plt.xlabel("Filling Fraction")
        plt.title("Work Done per Unit Mass Against Filling Fraction")
        plt.show()
    
    def graph_WD_FF(self):
        x,y=self.findtotalWD()
        plt.plot(x,y)
        plt.ylabel("Work Done (Joules)")
        plt.xlabel("Filling Fraction")
        plt.title("Work Done Against Filling Fraction")
        plt.show()
        

        

calc=WDCalc()