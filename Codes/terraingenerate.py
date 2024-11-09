import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sheetpath="Sheets/geodata.xls"
df=pd.read_excel(sheetpath,sheet_name="Sheet1")
print(df)
X=df["Distance (miles)"]*1.60934
Z=df["Elevation (ft)"]*0.0003048
plt.plot(X,Z,color="gray")
plt.xlabel("PIPE LENGTH (KM)")
plt.ylabel("ELEVATION(KM)")
plt.title("ACTUAL TERRAIN")
plt.show()
