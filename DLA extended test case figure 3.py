# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:09:36 2022

@author: ppyma4
"""
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(109)

N = 1000 #length and width of lattice
Np = 5000 #numer of particles
xycentre = N//2 #position of seed
lattice = np.zeros((N, N)) 
lattice[xycentre, xycentre] = 1 #put seed in lattice centre

xarray = ([]) 
yarray = ([])
xarray = np.append(xarray, xycentre) #append seed
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
            
            if R < position*relinj: #create new injection radius if stuck particle is furthest from the seed
                R = position*relinj
                kill = position*relkill
                
            n = 1 #end while loop
    
#%%
#adjust markersize for plot etc
plt.figure(figsize=(14,9))

plt.plot(yarray,xarray, '.', color = 'black', zorder = 0, label = 'stuck particles', markersize = 1.5)
plt.plot(yarray[0],xarray[0], 'o', color = 'red', markersize = 1.5, zorder = 10, label = 'seed particle')

plt.xlabel('$y$', fontsize = 17)
plt.ylabel('$x$', fontsize = 17)
plt.tick_params(labelsize = 17)
plt.title('N = 5000', fontsize = 17)
plt.axis('equal')

theta = np.linspace( 0 , 2 * np.pi , 1000 )
xinj = R * np.cos(theta) + 500
yinj = R * np.sin(theta) + 500
plt.plot(yinj, xinj, color = 'green', label = 'injection circle')

xkill = (kill) * np.cos(theta) + 500
ykill = (kill) * np.sin(theta) + 500
plt.plot(ykill, xkill, color = 'orange', label = 'kill circle')

plt.legend(fontsize = 17)