# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:10:38 2019

@author: slaxman
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import time
from plotly.offline import plot


start = time.time()

#reading the csv measurement file
data = pd.read_csv('DATA.csv', header = None)

phi = np.asarray(data[0].iloc[1:,0])
theta = np.asarray(data[0].iloc[0,1:])
power = np.asarray(data[0].iloc[1:,1:])

power = np.power(10,power*0.1)#converting from db to watt


#converting from spherical to cartesian coords
X = []
Y = []
Z = []


THETA = []
PHI = []
R = []

for p in range(0, len(phi)):
    
    for t in  range(0,len(theta)):
        
        PHI.append(float(phi[p]))
        
        THETA.append(float(theta[t]))
        R.append(float(power[p,t]))


THETA = np.deg2rad(np.asarray(THETA))
PHI = np.deg2rad(np.asarray(PHI))
R = np.asarray(R)


THETA = THETA.reshape(power.shape[0],power.shape[1])
PHI = PHI.reshape(power.shape[0],power.shape[1])
R = R.reshape(power.shape[0],power.shape[1])


X = R * np.sin(THETA) * np.cos(PHI)

Y = R * np.sin(THETA) * np.sin(PHI)

Z = R * np.cos(THETA) 

X = X.reshape([power.shape[0],power.shape[1]])
Y = Y.reshape([power.shape[0],power.shape[1]])
Z = Z.reshape([power.shape[0],power.shape[1]])

#setup layout and plot on 3d surface

layout = go.Layout(title="3D Radiation Pattern of 5G CW data")

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, surfacecolor=R, colorscale='Reds')], layout = layout)

plot(fig)

print("Time elapsed: ",time.time() - start, " seconds")
