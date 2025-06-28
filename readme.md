---
title: ALASKA PIPELINE PROJECT

---

# ALASKA PIPELINE PROJECT
This is official repo of the alaska pipeline project made for the course of fluid mechanics.
## ASSUMPTIONS
1. Pipeline is straight and have sape as per the terrain.
2. Bernoulli's Theorem hold for the flow.
3. Tempreature is maintained at 30 $^\circ$C.
4. The pipeline is always full. (No two-phase flow)
## Implementation
### STRAIGHT LEVEL PIPELINE WITH INFINITE THICKNESS
### Case 1
#### Diameter=12.7mm $\left(\frac{1}{2}\right)$ inch
#### VFL=1.3 million barrels per day output from the pipeline=$1.3*10^6*158.987$ liters/day=$206.6831*10^6$ liters/day=$2392.166$ liters/second=2.393 m^3^/s
#### Velocity Of Flow=18890.584 m/s
**This velocity is quite large and cannot be used in real life applications. So this diameter of pipe is unrealistic and irrelevant.**

Lets now assume velocity to be 2 m/s and find the diameter of pipe.
### Case 2
#### Velocity of Flow = 2 m/s (Assumed)
#### VFL = 2.393 m^3^/s
#### Diameter of Pipe (calculated) = 48.6 inch $\approx$ 48 inch $\approx$ 1.219 m 
#### $R~e~=\frac{\rho*V*D}{\mu}$ = $\frac{860*2*1.219}{5.64*10^{-3}}$ = 371751.773
Hence, the flow is turbulent.
Lets find the f~D~ value.
$f_D=0.046*R_e^{-0.2}$
$f_D=0.046*371751.773^{-0.2}$
$f_D=3.5736*10^{-3}$

Lets calculate friction head as function of length
$h_f=4*\frac{f}{g}*\frac{\Delta x}{D}*\frac{V^2}{2}$
$h_f=4*\frac{3.5736*10^{-3}}{9.81}*\frac{\Delta x}{1.219}*\frac{(2)^2}{2}$
$h_f=2.3666*10^{-3} \Delta x$ meter 

Lets simulate this value for our pipeline length of 800 miles i.e. 1287 KM
Lets assume line have only one pump at the start of line.
The graph is result obtained from using bernoulli's equation for pressure drop along pipeline
$P=P_{initial}-h_f*\rho*g$
The Profile found is as follows:
![Pressure profile without pumps](https://hackmd.io/_uploads/BJmENHpgyx.png)

Now lets consider addition of additonal pumps to keep pressure above 1 atm in pipes. We will add a pump when pressure drops below 1.2 atm.
By using above correction and the equation 
$P=P_{initial}-h_f*\rho*g+W_{pump}* \rho*g$
We get the following graph
![Pressure Profile With Pump](https://hackmd.io/_uploads/HJz1UBTeJl.png)

Hence this complete our model of level pipe system.
***
### STRAIGHT PIPELINE ELEVATED WITH INFINITE THICKNESS
Now let's consider our path have two mountains in our path. Our new terrain data is shown in the graph below.
![image](https://hackmd.io/_uploads/SJq0CCjWJl.png)
Now, Let's solve bernoulli's equation for this process
$$\Delta P+\rho* g*\Delta* Z=- h_f*\rho* g$$$$P=P_{initial}- h_f*\rho* g-\rho* g*\Delta Z$$Let's use this equation and terrain data and plot the graph between pressure inside pipe over span of pipeline. The Graph obtained is shown below.
![Elevated Pipe Without Pump](https://hackmd.io/_uploads/BykxJknb1e.png)
Now lets consider addition of additonal pumps to keep pressure above 1 atm in pipes. We will add a pump when pressure drops below 1.2 atm.
By using above correction and the equation 
$$\Delta P+\rho* g*\Delta* Z=W_{pump}* \rho*g- h_f*\rho* g$$
$$P=P_{initial}- h_f*\rho* g-\rho* g*\Delta Z+W_{pump}* \rho*g$$The graph obtained is as follows
![Elevated Profile with pump](https://hackmd.io/_uploads/SJ_JE_cWyx.png)
***
### STRAIGHT PIPELINE ELEVATED ON ACTUAL TERRAIN WITH INFINITE THICKNESS
Now let's take the actual elevation data
The Elevation profile is shown below
![Screenshot 2024-11-09 130619](https://hackmd.io/_uploads/B1CpBz6Zkl.png)

Now using the formula
$$P=P_{initial}- h_f*\rho* g-\rho* g*\Delta Z+W_{pump}* \rho*g$$The graph obtained is as follows 
![Pressure Profile on Actual Terrain With Pump](https://hackmd.io/_uploads/SJ4oLGTZ1l.png)
With this our model of pipeline with infinite thickness is complete. Now in succeding section we'll work on pipeline with finite thickness
***
### STRAIGHT LEVEL PIPELINE WITH FINITE THICKNESS
Now let's consider the pipe as it is in real life. For this project we will consider pipe of two pipe thickness 0.462" and 0.562" and three grades of steel Grade 60, Grade 65, Grade 70. The design tensile stress data is as follows
|Grade|Tensile Stress(MPa)|
|:-----:|:----:|
|60|420|
|65|551.581|
|70|585.5| 

The thickness of Pipe is given by the formula
$t=\frac{P*D}{2*\sigma_{tensile}}$
Rearranging the equation,
$P_{max}=\frac{t_{max}*2*\sigma_{tensile}}{D}$
Using the above equation we get the following data
| Steel Grade|Maximum Pressure (atm) for 0.462" thick pipe|Maximum Pressure (atm) for 0.562" thick pipe|
|:----:|:----:|:---:|
|60|79.80|97.08|
|65|104.1|127.49|
|70|111.255|135.33|

But, it is standard practise to take 30% excess pressure for safety purpose. By considering 30% less pressure from above values we get the following data.
| Steel Grade|Maximum Pressure (atm) for 0.462" thick pipe|Maximum Pressure (atm) for 0.562" thick pipe|
|:----:|:----:|:---:|
|60|61.39|74.68|
|65|80.623|98.07|
|70|85.581|104.103|

So lets develop model considering Straight pipe with 0.462" thickness.
For pressure reduction we'll add a orifice which will make a pressure drop of 200 psi i.e. 13.61 atm.
Considering the following assumptions the graphs obtained are shown below 
#### Grade 60 Pipe 0.462" thick pipe
![RealPipeGrade60D462](https://hackmd.io/_uploads/H1x-MI7fyg.png)
#### Grade 65 Pipe 0.462" thick pipe
![RealPipeGrade65D462](https://hackmd.io/_uploads/ryOmz8QzJl.png)

#### Grade 70 Pipe 0.462" thick pipe
![RealPipeGrade70D462](https://hackmd.io/_uploads/rJ1EMIXz1l.png)

#### Grade 60 Pipe 0.562" thick pipe
![RealPipeGrade60D562](https://hackmd.io/_uploads/r1FVzUQfJg.png)

#### Grade 65 Pipe 0.562" thick pipe
![RealPipeGrade65D562](https://hackmd.io/_uploads/Sk-Sf8Qzyg.png)

#### Grade 70 Pipe 0.562" thick pipe
![RealPipeGrade70D562](https://hackmd.io/_uploads/rk-wfU7fJl.png)


