import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import pandas as pd
''' 
CONSIDERING LEVEL PIPELINE CARRYING CRUDE OIL WITH VELOCITY 2 M/S 
REST ALL THINGS CALCULATED AS DESCRIBED IN README.MD  
'''
PaToAtm=9.8692e-6 #pascal to atm conversion factor e-6 means 10^-6
RHO=865           # DENSITY OF OIL (kg/m^3)
g=9.81            # ACCELERATION DUE TO GRAVITY (m/s^2)
FHeadPerMeter=0.0023666 # FRICTIONAL HEAD LOSS(m)

''' Lets assume only one pump(1000 psi)connected to the system at the initial location X=0 '''

P_inital=68.046  #atm

#defining arrays for storing pipeline length, Pressure values, and Friction losses 
X=np.arange(0,1289,1) # ARRAY OF DISTANCES (KM)
P=np.zeros(X.shape)      # ARRAY OF PRESSURE (m)
FLoss=np.zeros(X.shape)  # ARRAY OF FRICTIONAL LOSSES (m)

# LOOP FOR CALCULATIONS
i=0 # Indexing variable
for d in X :
    FLoss[i]=RHO*g*FHeadPerMeter*d*PaToAtm*1000 #Pascals converted to atm
    P[i]=P_inital-FLoss[i]
    i+=1

# def plain_format(x, pos): #Function to format numbers for graph
#     return f'{x}'  

# PLOTTING THE GRAPH
   
plt.plot(X,P,"g")   # Plot the Graphsx
plt.ylim((-200,80)) # Set Y axis limit
plt.xlim((0,1400)) # Set X axis limit
plt.gca().yaxis.set_major_locator(tk.MultipleLocator(20)) #set least count of axis 20
plt.gca().xaxis.set_major_locator(tk.MultipleLocator(100))
plt.xlabel("Pipe Length (Km)")      #setting labels
plt.ylabel("Pressure Inside Pipe (atm)")#setting labels
plt.title("PRESSURE INSIDE PIPE WITHOUT USING INLINE PUMP") #setting labels
plt.show()  # Show the graph

# Sheet export
data=np.vstack((X,FLoss,P))
df=pd.DataFrame(data.transpose(),columns=["Pipe Length (Km)","Friction Pressure Loss (atm)","Resultant Pressure (atm)"])
df.to_excel("Pressure_Profile_Without_Inline_Pump.xlsx",index=False)