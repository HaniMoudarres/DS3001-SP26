"""
Homework 1 Question 2
"""
# Import numpy for proper math functionality and matplotlib for plotting points
import numpy as np
import matplotlib.pyplot as plt

# Create plot from 0 to 1 with 50 evenly space points
x = np.linspace(0,1, 50)

# Natural log values
y = np.array([np.log(x)])

# Exponential Values
z = np.array([np.exp(x)])

# Plot both the log and exponential functions
plt.scatter(x,y, label='Natural Log')
plt.scatter(x,z, label='Exponential')

#label x-axis
plt.xlabel("x-axis")

#label y-axis
plt.ylabel("y-axis")

#Title of graph
plt.title("Natural Log and Exponential Functions")

# Creates legend in lower right of plot
plt.legend(loc = 'lower right')

# Create the plot
plt.show()


"""
Part 2 of Question 2, Graphing Sine and Cosine Functions (parts 8-12 of the assignment)
"""
# Create plot from -6.5 to 6.5 with 100 evenly spaced points
x = np.linspace(-6.5, 6.5, 100)

# Sine function values
y = np.sin(x)

# Cosine Function Values
z = np.cos(x)

# Plot both the Sine and Cosine functions as scatter plots
plt.scatter(x,y, label='Sine Funciton')
plt.scatter(x,z, label='Cosine Function')

# Formatting and labeling the graph
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sine and Cosine Functions")
plt.legend(loc = 'lower right')

# Create the plot
plt.show()

# Plot both the Sine and Cosine functions as line graphs
plt.plot(x,y, label='Sine Funciton')
plt.plot(x,z, label='Cosine Function')

# Formatting and labeling the graph
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sine and Cosine Functions")
plt.legend(loc = 'lower right')

# Create the plot
plt.show()