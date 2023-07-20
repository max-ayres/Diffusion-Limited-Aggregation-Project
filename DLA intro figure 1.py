# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:50:24 2022

@author: Maximilian
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1000)

N = 16 #size of lattice
Np = 30 #number of particles
centre = N//2

particlesx = ([])
particlesy = ([])
particlesx = np.append(particlesx, centre) #append seed
particlesy = np.append(particlesy, centre)

for i in range(Np):
    n = 0 #start while loop

    pos = np.random.randint(0,4) #inject particles at boundary
    if pos == 0: 
        xs = np.random.randint(0,N-1)
        ys = 0
    elif pos == 1:
        xs = 0
        ys = np.random.randint(0,N-1)
    elif pos == 2:
        xs = np.random.randint(0,N-1)
        ys = N-1
    elif pos == 3:
        xs = N-1
        ys = np.random.randint(0,N-1)
        
    while n == 0:   
        random = np.random.randint(0, 4)
        if random == 0: #random walk of particle
            xs = xs + 1 
            xs = xs - (N+1)*(xs==N+1) #periodic lattice
        elif random == 1:
            ys = ys + 1
            ys = ys - (N+1)*(ys==N+1)
        elif random == 2:
            xs = xs - 1
            xs = xs + (N+1)*(xs==-1)
        elif random == 3:
            ys = ys - 1
            ys = ys + (N+1)*(ys==-1)
            
        for z in range(i+1): #while loop for finding if nearest neighbours are hit
            if (xs == particlesx[z] and ys == particlesy[z] + 1) or (xs == particlesx[z] and ys == particlesy[z] - 1) or (xs == particlesx[z] + 1 and ys == particlesy[z]) or (xs == particlesx[z] - 1 and ys == particlesy[z]):
                
                particlesx = np.append(particlesx, xs) #append to particle arrays
                particlesy = np.append(particlesy, ys) 

                n = 1 #end while loop

#%%
plt.figure(figsize=(14,9))
ax = plt.axes()

for w in range(len(particlesx)): #finding the nearest neighbours of all particles
    ax.plot(particlesy[w]+1, particlesx[w], 'x', color='orange')
    ax.plot(particlesy[w]-1, particlesx[w], 'x', color='orange')
    ax.plot(particlesy[w], particlesx[w]+1, 'x', color='orange')
    ax.plot(particlesy[w], particlesx[w]-1, 'x', color='orange')

ax.plot(1000, 1000, 'x', color = 'orange', label = 'sticking point') #used for creating legend
ax.plot(1000, 1000, 's', color = 'black', label = 'stuck particle')
ax.plot(1000, 1000, 's', color = 'red', label = 'seed particle')

ax.plot(particlesy, particlesx, 's', color='black', markersize = 33)
ax.plot(particlesy[0], particlesx[0], 's', color='red', markersize = 33)

ax.axis('square')
ax.tick_params(axis = 'both', labelsize = 17)
ax.set_xlim(0,N-1)
ax.set_ylim(0,N-1)
ax.set_xlabel('$y$', fontsize = 17)
ax.set_ylabel('$x$', fontsize = 17)

ax.legend(fontsize = 17)