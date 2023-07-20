# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:50:46 2022

@author: ppyma4
"""

import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1234)

N = 10000 #length and width of lattice
Np = 20000 #numer of particles injected
xycentre = N//2 #position of seed particle
lattice = np.zeros((N, N)) 
lattice[xycentre, xycentre] = 1 #seed particle

xarray = ([]) 
yarray = ([])
xarray = np.append(xarray, xycentre)
yarray = np.append(yarray, xycentre)

R = 6 #initial injection radius
kill = 8 #initial kill radius
relkill = 2.3 #value required to set new kill radius
relinj = 2 #value to required to set new injection radius

for i in range(Np):
    n = 0 #start while loop
    
    randomtheta = np.random.uniform(0, 2*np.pi) #spawns random particle on injection circle
    xs = round(R*np.cos(randomtheta)) + xycentre
    ys = round(R*np.sin(randomtheta)) + xycentre
    
    while n == 0:   
        random = np.random.randint(0, 4)
        if random <= 1: #random walk of particle
            xs = (xs + 1)*(random == 0) + (xs - 1)*(random == 1)
        else:
            ys = (ys + 1)*(random == 2) + (ys - 1)*(random == 3)

        position = (xs-xycentre)**2 + (ys-xycentre)**2 #not rooted as makes code run faster, kill is squared to compensate this

        if (position >= kill**2): #reinject particle back into injection radius if touches kill circle
            randomtheta = np.random.uniform(0, 2*np.pi)
            xs = round(R*np.cos(randomtheta)) + xycentre
            ys = round(R*np.sin(randomtheta)) + xycentre
        elif lattice[xs+1, ys] == 1 or lattice[xs-1, ys] == 1 or lattice[xs, ys+1] == 1 or lattice[xs, ys-1] == 1: #finding if particle has hit sticking point
            
            lattice[xs, ys] = 1 #set point in lattice to equal one
            
            position = np.sqrt(position)
            
            xarray = np.append(xarray, xs)
            yarray = np.append(yarray, ys)
            
            if R < position*relinj: #create new injection radius if stuck particle is furthest from seed 
                R = position*relinj
                kill = position*relkill
                
            n = 1 #end while loop

#%%
#adjust markersize for plot etc
plt.figure(figsize = (14, 9))
ax2 = plt.axes()
ax2.plot(yarray,xarray, 'o', color = 'black', markersize = 0.75)

ax2.axis('equal')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_xticks([])
ax2.set_yticks([])