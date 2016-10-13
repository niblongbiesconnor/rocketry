"""
Calculates the rocket's total work done
"""

from matplotlib.pyplot import plot, show

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
        
    def workdone(self, f):
        """
        Calculates work done for various values of f
        """
        # *10**-3 so as to convert units from litres to cubic metres
        top = self.P * self.V * (10**-3)
        bottom = (-self.gamma+1) * ((1-f)**self.gamma)-(1-f)
        w = top / bottom
        return w 
    
    def WDweightratio(self,f):
        """
        Calculate the work done per kilogram of mass
        """
        workdone = self.workdone(f)
        bottom = (f * self.V * (10**-3) * self.rho) + 0.1
        wk = workdone / bottom
        return wk
    
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
