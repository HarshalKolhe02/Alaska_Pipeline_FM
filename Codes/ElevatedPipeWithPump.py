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
Z=np.zeros(X.shape)
Z1=np.sin(np.radians(np.concatenate((np.linspace(0,90,45),np.linspace(90,180,46)))))
Z2=np.sin(np.radians(np.concatenate((np.linspace(0,90,45),np.linspace(90,180,46)))))
print(Z.shape)
Z[400:400+len(Z1)]=Z1
Z[700:700+len(Z2)]=Z2
P=np.zeros(X.shape)      # ARRAY OF PRESSURE (m)
FLoss=np.zeros(X.shape)  # ARRAY OF FRICTIONAL LOSSES (m)
Pump=np.empty(X.shape)
Pump[:]=np.nan
# LOOP FOR CALCULATIONS
i=0 # Indexing variable
for d in X :
    FLoss[i]=RHO*g*FHeadPerMeter*d*PaToAtm*1000 #Pascals converted to atm
    P[i]=P_inital-FLoss[i]-RHO*g*Z[i]*PaToAtm*1000 
    if P[i]<1.2 :
        P_inital+=68.046
        Pump[i]=P[i-1]
        P[i]=P_inital-FLoss[i]-RHO*g*Z[i]*PaToAtm*1000 
    i+=1

# def plain_format(x, pos): #Function to format numbers for graph
#     return f'{x}'  
# PLOTTING THE GRAPH
plt.plot(X,P,"g")   # Plot the Graphsx
plt.ylim((-20,130)) # Set Y axis limit
plt.xlim((0,1400)) # Set X axis limit
plt.gca().yaxis.set_major_locator(tk.MultipleLocator(5)) #set least count of axis 20
plt.gca().xaxis.set_major_locator(tk.MultipleLocator(100))
plt.plot(X,Pump,"Hr")
plt.xlabel("Pipe Length (Km)")      #setting labels
plt.ylabel("Pressure Inside Pipe (atm)")#setting labels
plt.title("PRESSURE INSIDE PIPE WITH PUMPS ON ELEVATED TERRAIN") #setting labels
plt.legend(["Pressure Profile","Pump Locations"])
ax2 = plt.gca().twinx()
ax2.plot(X, Z,color="gray",linestyle="dashed", label="ELEVATION (In KM)")
ax2.set_ylabel("ELEVATION", color="gray")
ax2.tick_params(axis="y", labelcolor="gray")
plt.show()  # Show the graph


# Sheet export
data=np.vstack((X,Z,FLoss,P,Pump))
df=pd.DataFrame(data.transpose(),columns=["Pipe Length (Km)","Elevation(Km)","Friction Pressure Loss (atm)","Resultant Pressure (atm)","Pump"])
df=df.fillna(0)
df["Pump"]=df["Pump"].where(df["Pump"]==0,"ONE PUMP ADDED")
print(df)
df.to_excel("Pressure_Profile_With_Pump_Elevated.xlsx",index=False)