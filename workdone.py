#calculates the rockets total work done#
from matplotlib.pyplot import plot, show;
class WDCalc:
    def __init__(self):        
      self.gamma=1.4 #the ratio of specific heat transfer
      self.filling_fraction_list=[]#the list of all the times        
      self.workdone_list=[]#the function of those times        
      self.P=4*(10**5) #the pressure of the air in the bottle        
      self.V=2*(10**-3) #the volume of the bottle in litres        
      self.rho=1#the density of the liquid currently water
    def workdone(self,f):       
      #*10**-3 so as to convert units        
      w=((self.P*self.V*(10**-3))/(-self.gamma+1))*(((1-f)**self.gamma)-(1-f))        
      return(w)
    def WDweightratio(self,f):         
      wk=self.workdone(f)/((f*self.V*(10**-3)*self.rho)+0.1)         
      #the work done per kilo is wk         
      return wk
    def findtotalWDMR(self):        
      for i in range(1,1001):             
        f=i*0.001             
        x=self.WDweightratio(f)             
        self.filling_fraction_list.append(f)             
        self.workdone_list.append(x)             
        return self.filling_fraction_list, self.workdone_list
