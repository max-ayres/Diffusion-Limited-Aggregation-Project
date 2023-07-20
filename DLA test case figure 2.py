# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

N = 11 #size of lattice

xs = np.array([0, 0, 0, 10, 10, 10, 2, 6, 3, 6]) #particle starting positions
ys = np.array([0, 5, 10, 0, 6, 10, 0, 0, 10, 10])

particles = np.zeros((2, 11)) #array for particle stuck position
particles[:,0] = 5, 5 #seed coordinates

for i in range(10):
    n = 0 #start while loop
    
    while n == 0:
        random = np.random.randint(0, 4)
        if random == 0: #random walk of particle
            xs[i] = xs[i] + 1 
            xs[i] = xs[i] - 11*(xs[i]==11) #periodic lattice
        elif random == 1:
            ys[i] = ys[i] + 1
            ys[i] = ys[i] - 11*(ys[i]==11)
        elif random == 2:
            xs[i] = xs[i] - 1
            xs[i] = xs[i] + 11*(xs[i]==-1)
        elif random == 3:
            ys[i] = ys[i] - 1
            ys[i] = ys[i] + 11*(ys[i]==-1)
            
        for z in range(i+1): #while loop for finding if nearest neighbours are hit
            if (xs[i] == particles[0,z] and ys[i] == particles[1,z] + 1) or (xs[i] == particles[0,z] and ys[i] == particles[1,z] - 1) or (xs[i] == particles[0,z] + 1 and ys[i] == particles[1,z]) or (xs[i] == particles[0,z] - 1 and ys[i] == particles[1,z]):
                
                particles[0,i+1] = xs[i] #append to particle arrays
                particles[1,i+1] = ys[i] 

                n = 1 #end while loop

#%%
plt.figure(figsize=(14,9)) #plot test case
ax = plt.axes()

ax.plot(particles[1,:], particles[0,:], 's', markersize = 50, color = 'black')

ax.axis('square')
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
ax.tick_params(axis = 'both', labelsize = 17)

ax.set_ylabel('$x$', fontsize = 17)
ax.set_xlabel('$y$', fontsize = 17)

ax.invert_yaxis()