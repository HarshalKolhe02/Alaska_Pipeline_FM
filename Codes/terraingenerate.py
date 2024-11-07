import numpy as np
import matplotlib.pyplot as plt

#defining arrays for storing pipeline length, Elevation with two mountains 
X=np.arange(0,1289,1) # ARRAY OF DISTANCES (KM)
Z=np.zeros(X.shape)
Z1=np.sin(np.radians(np.concatenate((np.linspace(0,90,45),np.linspace(90,180,46)))))
Z2=np.sin(np.radians(np.concatenate((np.linspace(0,50,20),np.full((1,),50),np.linspace(50,0,30)))))
print(Z.shape)
Z[200:200+len(Z1)]=Z1
Z[420:420+len(Z2)]=Z2
print(Z)
plt.plot(X,Z,"r")
plt.xlabel("PIPELINE LENGTH")
plt.ylabel("ELEVATION")
plt.title("ELEVATION DATA")
plt.show()
