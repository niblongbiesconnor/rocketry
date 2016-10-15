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
        # Pressure of air in bottle at the moment about 3 atmospheres
        self.P=4*(10**5)
        # Pressure of the atmosphere currently at an altitude of 0m above sea level
        self.Patm=101325
        # Volume of bottle (litres)
        self.V=2*(10**-3) 
        # Density of liquid
        # Currently water
        self.rho=1
        #The total mass of the rocket when empty
        self.mass_rocket=10
    def WDgasblast(self,f):
        """
        calculates the work done in the gas blast
        """
        #10**3 to convert units
        part1=(self.P*self.V)/(-self.gamma+1)
        part2=(1-f)**(-self.gamma+1)
        part3=(self.P/self.Patm)**((1/self.gamma)-1)
        part4=(part2*part3)-1
        workdone=part1*part4
        return workdone
        
    def workdone(self, f):
        """
        Calculates work done for various values of f
        """
        top = self.P * self.V*(((1-f)**self.gamma)-(1-f))
        bottom = (-self.gamma+1)
        workdone = top / bottom
        workdone+=(self.WDgasblast(f))
        return workdone
    
    def WDweightratio(self,f):
        """
        Calculate the work done per kilogram of mass
        """
        workdone = self.workdone(f)
        #V*10**3 as converting back into litres from cubic metres as defined 
        mass = (f * self.V*(10**3)*self.rho) + self.mass_rocket
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
