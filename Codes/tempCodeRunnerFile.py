# # Sheet export
# data=np.vstack((X,FLoss,Pump,Pump_Work,P))
# df=pd.DataFrame(data.transpose(),columns=["Pipe Length (Km)","Friction Pressure Loss (atm)","Pump","Pump Pressure","Resultant Pressure (atm)",])
# df=df.fillna(0)
# df["Pump"]=df["Pump"].where(df["Pump"]==0,"ONE PUMP ADDED")
# print(df)
# df.to_excel("Pressure_Profile_With_Pump.xlsx",index=False)