# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:09:36 2022

@author: ppyma4
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

N = 1000 #size of lattice
Np = 2000 #numer of particles
cluster = 50 #numer of clusters averaged over
xycentre = N//2

rarray = ([]) #radius array
rarray = np.append(rarray, 0)

relkill = 2.3 #value required to set new kill radius
relinj = 2 #value to required to set new injection radius

Rarray = np.zeros(1500)#arrays for finding fractal dimension
Narray = np.zeros(1500)

for k in range(cluster):
    R = 6 #new injection radius
    kill = 8 #new injection radius

    lattice = np.zeros((N, N)) #new lattice
    lattice[xycentre, xycentre] = 1 #particle at center of new lattice[x, y]
    
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
            elif lattice[xs+1, ys] == 1 or lattice[xs-1, ys] == 1 or lattice[xs, ys+1] == 1 or lattice[xs, ys-1] == 1: #finding if particle has hit a sticking point
                
                lattice[xs, ys] = 1 #set stuck point in lattice to equal one
                
                position = np.sqrt(position)
                
                rarray = np.append(rarray, position)
                
                if R < position*relinj: #create new injection radius if stuck particle is furthest from the seed
                    R = position*relinj
                    kill = position*relkill
                    Rmax = position
                    
                n = 1 #end while loop      
    
    for r in range(4, round(Rmax)*4): #find number of particle beneath max radius for intervals of 0.25
        Rarray[r-1] = Rarray[r-1] + (r/4)
        Narray[r-1] = Narray[r-1] + np.sum(r/4 >= rarray) #number of particles smaller than radius r

Rarray = np.trim_zeros(Rarray)#remove zeros from the end of arrays
Narray = np.trim_zeros(Narray)

Rarray = Rarray/cluster#find average of r and N arrays
Narray = Narray/cluster

#%%
#adjust gradient
up  = 0.27
down = 0.05
gradR = Rarray[round(down*len(Rarray)):round(up*len(Rarray))]#array slice to gradient arrays so only linear part of graph is calculated
gradN = Narray[round(down*len(Narray)):round(up*len(Narray))]

logrplot = np.log(Rarray)
logNplot = np.log(Narray)
logr = np.log(gradR)
logN = np.log(gradN)

errorpercent = 1.5/Narray #percentage uncertainty assuming plus or minus 1.5 particles 
yerr = (errorpercent*logNplot)/np.sqrt(cluster) #standard error

plt.figure(figsize=(14,9))
ax = plt.axes()

ax.set_ylabel('$ln(N)$', fontsize = 17)
ax.set_xlabel('$ln(R)$', fontsize = 17)
ax.tick_params(axis = 'both', labelsize = 17)
ax.set_title('N = 2000   Clusters = 50', fontsize = 17)

m = ((np.mean(logr)*np.mean(logN)) - np.mean(logr*logN)) / ((np.mean(logr)*np.mean(logr)) - np.mean(logr**2)) #line and intercept of best fit
c = np.mean(logN) - m*np.mean(logr) #https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/

ax.errorbar(logrplot, logNplot, yerr = yerr, capsize = 5, color='black', fmt = '.', zorder = 0)
ax.plot(logr, m*logr+c, color='orange', linewidth = 3, zorder = 10)

print(m)