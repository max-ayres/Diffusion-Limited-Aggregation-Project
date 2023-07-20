# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:09:36 2022

@author: ppyma4
"""
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

np.random.seed(1234)

N = 1000 #size of lattice
Np = 5000 #numer of particles
xyzcentre = N//2
lattice = np.zeros([N, N, N]) 
lattice[xyzcentre, xyzcentre, xyzcentre] = 1 #seed particle

rarray = ([])
xarray = ([])
yarray = ([])
zarray = ([])
rarray = np.append(rarray, 0)
xarray = np.append(xarray, xyzcentre)
yarray = np.append(yarray, xyzcentre)
zarray = np.append(zarray, xyzcentre)

R = 6 #initial injection radius
kill = 8 #initial kill radius
relkill = 2.3 #value required to set new kill radius
relinj = 2 #value to required to set new injection radius

for i in range(Np): #particle
    n = 0 #start while loop
    
    randomtheta = np.random.uniform(0, 2*np.pi) 
    randomphi = np.random.uniform(0, np.pi)
    
    xs = round(R*np.sin(randomtheta)*np.cos(randomphi)) + xyzcentre #spawn particles on injection sphere
    ys = round(R*np.sin(randomtheta)*np.sin(randomphi)) + xyzcentre
    zs = round(R*np.cos(randomtheta)) + xyzcentre
    
    while n == 0:   
        random = np.random.randint(0, 6)
        if random <= 1: #random walk of particle
            xs = (xs + 1)*(random == 0) + (xs - 1)*(random == 1)
        elif random == 2 or random == 3:
            ys = (ys + 1)*(random == 2) + (ys - 1)*(random == 3)
        elif random == 4 or random == 5:
            zs = (zs + 1)*(random == 4) + (zs - 1)*(random == 5)
                
        position = (xs-xyzcentre)**2 + (ys-xyzcentre)**2 + (zs-xyzcentre)**2  #not rooted as makes code run faster, kill is squared to compensate this

        if (position >= kill**2): #reinject particle back into injection sphere if touching kill sphere
            randomtheta = np.random.uniform(0, 2*np.pi) 
            randomphi = np.random.uniform(0, np.pi)
            xs = round(R*np.sin(randomtheta)*np.cos(randomphi)) + xyzcentre
            ys = round(R*np.sin(randomtheta)*np.sin(randomphi)) + xyzcentre
            zs = round(R*np.cos(randomtheta)) + xyzcentre         
        elif lattice[xs+1, ys, zs] == 1 or lattice[xs-1, ys, zs] == 1 or lattice[xs, ys+1, zs] == 1 or lattice[xs, ys-1, zs] == 1 or lattice[xs, ys, zs+1] == 1 or lattice[xs, ys, zs-1] == 1:
            
            lattice[xs, ys, zs] = 1 #set point in lattice to equal one
            position = np.sqrt(position)
            
            xarray = np.append(xarray, xs)
            yarray = np.append(yarray, ys)
            zarray = np.append(zarray, zs)
            rarray = np.append(rarray, position)
            
            if R < position*relinj: 
                R = position*relinj 
                kill = position*relkill
                Rmax = position
                
            n = 1 #end while loop
    
Rarray = ([])
Narray = ([])    

for r in range(4, round(Rmax)*4): #find number of particle beneath max radius for intervals of 0.25
    Rarray = np.append(Rarray, r/4)
    Narray = np.append(Narray, np.sum(r/4 >= rarray)) #number of particles smaller than radius r
    
#%%
#adjust markersize for plot  and gradient
down = 0.1
up = 0.3
gradR = Rarray[round(down*len(Rarray)):round(up*len(Rarray))]#array slice to plot gradient for linear part of graph
gradN = Narray[round(down*len(Narray)):round(up*len(Narray))]

logrplot = np.log(Rarray)
logNplot = np.log(Narray)
logr = np.log(gradR)
logN = np.log(gradN)

errorpercent = 1.5/Narray
yerr = (errorpercent*logNplot)

plt.figure(figsize = (14, 9))
ax = plt.axes([0.5,0.3,0.45,0.4])

ax.set_ylabel('$ln(N)$', fontsize = 17)
ax.set_xlabel('$ln(R)$', fontsize = 17)
ax.tick_params(axis = 'both', labelsize = 17)

m = ((np.mean(logr)*np.mean(logN)) - np.mean(logr*logN)) / ((np.mean(logr)*np.mean(logr)) - np.mean(logr**2)) #line and intercept of best fit
c = np.mean(logN) - m*np.mean(logr) #https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/

ax.errorbar(logrplot, logNplot, yerr = yerr, capsize = 2, fmt = '.', color='black', zorder = 0)
ax.plot(logr, m*logr+c, color = 'orange', zorder = 10, linewidth = 2.5)


ax2 = plt.axes([-.09,0.2,0.6,0.6], projection = '3d')
ax2.scatter3D(yarray, xarray, zarray, s = 8, color = 'white', edgecolor = 'black')

ax2.set_xlim(460,540)
ax2.set_ylim(460,540)
ax2.set_zlim(460,540)
ax2.set_xlabel('$y$', fontsize = 17)
ax2.set_ylabel('$x$', fontsize = 17)
ax2.set_zlabel('$z$', fontsize = 17)
ax2.tick_params(labelsize = 10)
ax2.set_title('N = 5000', fontsize = 17)

print(m)
