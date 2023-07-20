# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:09:36 2022

@author: ppyma4
"""
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1234)

latw = 301 #y
lath = 600 #x
Np = 4000 #numer of particles
lattice = np.zeros((lath, latw))
lattice[0,0:,] = 1 #initial line seed

yarray = ([])
xarray = ([])

height = 3 #initial injection height
kill = 5 #initial kill height

relheight = 2 #value required to set new injection height
relkill = 2.2 #value required to set new kill height

for i in range(Np): #particle

    n = 0 #start while loop
    
    ys = np.random.randint(1, latw - 2) #particle spawn position, cant be (0,300) as code will crash
    xs = height #inijection height
    
    while n == 0:   
        random = np.random.randint(0, 4)
        if random == 0:
            xs = xs + 1
        elif random == 1:
            ys = ys + 1
            ys = ys - (latw - 3)*(ys >= latw - 2) #periodic lattice
        elif random == 2:
            xs = xs - 1
        else:
            ys = ys - 1
            ys = ys + (latw - 3)*(ys <= 1)
            
        if (xs >= kill): #reinject particle back into injection height if touch kill height
            ys = np.random.randint(1, latw - 2)
            xs = height
        elif lattice[xs+1, ys] == 1 or lattice[xs-1, ys] == 1 or lattice[xs, ys+1] == 1 or lattice[xs, ys-1] == 1: #condition for sticking a particle
            
            lattice[xs, ys] = 1
            
            xarray = np.append(xarray, xs)
            yarray = np.append(yarray, ys)

            if xs*2 >= height: #create new injection height if stuck particle is furthest from the seed
                Hmax = xs
                height = round(xs*relheight) 
                kill = round(xs*relkill)
                
            n = 1 #end while loop

Harray = ([]) 
Narray = ([])    

for H in range(4, round(Hmax/2)*4): #find number of particles for a given h beneath max height
    Harray = np.append(Harray, H/4)
    Narray = np.append(Narray, np.sum(H/4 >= xarray)) #number of particles smaller than height H

#%%
#adjuts markersize and gradient etc
plt.figure(figsize=(14, 9))

ax = plt.axes([0.08,0.3,0.4,0.4])
ax.plot(yarray, xarray, 'o', markersize = 1, color = 'white', zorder = 10, markeredgecolor = 'black', markeredgewidth = 1)
ax.plot(np.arange(0,latw+1, 0.1), np.zeros((latw+1)*10), 's', markersize = 1, color = 'red', zorder = 0) #plot initial seed

ax.set_title('N = 4000', fontsize = 17)
ax.axis('equal')
ax.set_xlabel('Width', fontsize = 17)
ax.set_ylabel('Height', fontsize = 17)
ax.tick_params(labelsize = 17)

up = 0.2
down = 0.02
gradH = Harray[round(down*len(Harray)):round(up*len(Harray))]
gradN = Narray[round(down*len(Narray)):round(up*len(Narray))]

logHplot = np.log(Harray)
logNplot = np.log(Narray)
logH = np.log(gradH)
logN = np.log(gradN)

errorpercent = 1.5/Narray
yerr = (errorpercent*logNplot)

ax2 = plt.axes([0.57,0.3,0.4,0.4])
ax2.errorbar(logHplot, logNplot, yerr = yerr, capsize = 1.5, fmt = '.', color='black', zorder = 0) #plot to find the the fractual dimension
ax2.set_ylabel('$ln(N)$', fontsize = 17)
ax2.set_xlabel('$ln(H)$', fontsize = 17)
ax2.tick_params(axis = 'both', labelsize = 17)

m = ((np.mean(logH)*np.mean(logN)) - np.mean(logH*logN)) / ((np.mean(logH)*np.mean(logH)) - np.mean(logH**2)) #line and intercept of best fit
c = np.mean(logN) - m*np.mean(logH) #https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/
ax2.plot(logH, m*logH+c, color='orange', zorder = 10, linewidth = 2)

print(m)