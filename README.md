# rocketry
A Python repository for rocketry simulation.
Currently this project is attempting to create a functional calculator of the work done by a water powered rocket.
It now also includes basic forces calculation programs such as air resistance and gravity calculators. I am now going to include functionality that will allow for the optimisation of the gas used.

It now also comes with a new program that finds the forces in a much more accurate way. This new file is now the primary concern of this project as the gas expansion model is only usefull for overall analysis. However as these processes are simply too complex to calculate mathematically the program uses a numerical analysis technique to find the height reached using a finite differencing scheme. 

My next steps are to debug the modelling program as it contains several errors.
