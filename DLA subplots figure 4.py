# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:09:36 2022

@author: ppyma4
"""
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1234)

N = 1000 #length and width of lattice
Np = np.array([500, 1000, 2000, 4000]) #numer of particles
xycentre = N//2 #position of center particle

title = np.array(['N=500', 'N=1000', 'N=2000', 'N=4000'])
markersize = np.array([3.3, 2.4, 0.9, 0.72])#markersize depending on particles plotted

relkill = 2.3 #value required to set new kill radius
relinj = 2 #value to required to set new injection radius

plt.figure(figsize=(14,9))

for k in range(4):
    xarray = ([])
    yarray = ([])
    xarray = np.append(xarray, xycentre)
    yarray = np.append(yarray, xycentre)
    
    R = 6 #initial injection radius
    kill = 8 #initial kill radius

    lattice = np.zeros((N, N)) 
    lattice[xycentre, xycentre] = 1 #particle at center of lattice[x, y]

    for i in range(Np[k]): #particle number
        n = 0 #start while loop
        
        randomtheta = np.random.uniform(0, 2*np.pi) #spawns random particle on injection radius
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
                
                if R < position*relinj: ##create new injection radius if stuck particle is furthest from the seed
                    R = position*relinj
                    kill = position*relkill
                
                n = 1 #end while loop
                
    plt.subplot(2, 2, k+1)

    plt.plot(yarray, xarray, 'o', color = 'white', markersize = markersize[k], markeredgecolor = 'black', markeredgewidth=1, zorder = 0)
    plt.plot(yarray[0],xarray[0], 'o', color = 'red', markersize = markersize[k], zorder = 10)
    
    plt.axis('equal')
    plt.tick_params(axis = 'both', labelsize = 17)
    plt.xlabel('$y$', fontsize = 17)
    plt.ylabel('$x$', fontsize = 17)
    plt.title(title[k], fontsize = 17)

plt.subplots_adjust(wspace = 0.31, hspace = 0.48)
