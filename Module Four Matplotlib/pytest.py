# A simple python script
import matplotlib.pyplot as plt
import numpy as np

# get a number from the user
f = float(input("Enter the frequency: "))
print("frequency is: {}".format(f))

d = float(input("Enter the decay constant: "))
print("decay constant is: {}".format(d))

# plot a couple functions, using the above input
x = np.linspace(0, 20, 300)
plt.plot(x, np.sin(f*x)*np.exp(-x/d))
plt.plot(x, np.exp(-x/d), c="r")
plt.plot(x, -np.exp(-x/d), c="r")

# need to tell python to SHOW the plot
plt.show()
