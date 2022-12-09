# Program to plot a cubic function
#
# Written by Ben Wheeler
# Culver-Stockton College    12/6/2017
from matplotlib.pylab import plot, show, title, xlabel, ylabel
#
# Specify x values to plot
xlabel("Independent Variable x",color="blue")
x = [-10.0,-9.0,-8.0,-7.0,-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
#
# Initialize y values list
y = [ ]
#
# Set up loop to calculate y values from y = x**3 - 3 x**2 + 3 x - 1
for xx in x:
    yy = xx**3 - 3*xx**2 + 3*xx-1
    y.append(yy)
# Set up Graph
#
title("Cubic Equation",color="blue",fontweight=16)
xlabel("Independent Variable x",color="blue")
ylabel("Dependent Variable y",color="blue")
plot(x,y,color="red",linestyle="--")
show()
