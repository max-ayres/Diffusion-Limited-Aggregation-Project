# Diffusion-Limited-Aggregation-Project

LOOK THROUGH THE PDF AND RUN ANY CODE INTERESTED IN USING THE INSTRUCTIONS BELOW, OTHERWISE CODE WILL RUN FOR OVER A MINUTE

Scientific computing degree level coursework
READ ME

Diffusion Limited Aggregation




Notes

The clusters were plotted with x on the y axis and y on the x axis as this is what the clusters looked like in the lattice.

Code takes a long time to run for a large amount of particles due to the relative injeciton radius being 
large for larger clusters. This gives more accurate results as there will be less of a bias (injecting particle from infininty)
, as with a smaller injection radius particles will tend to stick to the largest branch. Due to the time issue the relative
injection radius will need to be changed (stated in the instructions below), however, this will not make much of a difference.
This is the same reason for changing the relative kill radius (as particles must wander off to infinity to be killed).
More particles can be modelled with a smaller relative kill and injection radius, however, this will make it less accurate.

Do not change the figure size once they have loaded as this will mess up the sizes of the markers and particles and
will not look like they are touching.

#%% was used multiple times in the code as it was useful for adjusting gradients, markersizes etc once data had been generated

All code should take less than a minute to run

m (gradient) and c (y-intercept) equations were found from https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/




Instructions for code

DLA pretty plot figure 0.py
Set Np on line 14 to 1500, set relinj on line 27 to 1.5, set relkill on line 26 to 1.725, set the markersize on line to 68 to 2.2
Run the code above then the code below

DLA intro figure 1.py
Does not need changing, run the code above, then the code below

DLA test case figure 2.py
Does not need changing, run the code above, then the code below

DLA extended test case figure 3.py
Set Np on line 13 to 1500, set relkill on line 25 to 1.725, set relinj on line 26 to 1.5
Set title of line 73 to 'N = 1500'
run the code above then the code below

DLA subplots figure 4.py
Set Np on line 13 to np.array([250, 500, 750, 1000]) , set relkill on line 19 to 1.725, set relinj on line 20 to 1.5
Set title on line 16 to np.array(['N=250','N=500','N=750','N=1000'])
Run the code

DLA fractal dimension plot figure 5.py
Set Np on line 13 to 500, set relkill on line 20 to 1.725, set relinj on line 21 to 1.5, set cluster on line 14 to 10, set up on line 80 to 0.3
Set title  on line 99 to 'N = 500 Clusters = 10'
Run the code above then the code below

DLA 3D figure 6.py
Set Np on line 14 to 700, set relkill on line 30 to 1.725, set relinj on line 31 to 1.5, set up and down on lines 87 and 86 to 0.2 and 0.05
set s on line 114 to 15, set the axis limits on lines 116,117,118 to (485,535), set title on line 123 to 'N = 700'
Run the code above then the code below

DLA line seed figure 7.1.py
Set Np on line 14 to 2000
set title on line 70 to 'N = 2000'
Run the code above then the code below

DLA sticking probability figure 8.py
Change Np on line 13 to 400, set relkill on line 17 to 1.725, set relinj on line 18 to 1.5
set markersizes on lines 83 and 84 to 2.5
Run the code
