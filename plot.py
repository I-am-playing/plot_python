#!/usr/bin/env python3

import random
from itertools import count

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []

window=20
index = count(-1 * window,1)

def animate(i):

	# Generate data
	data = random.randint(0,10)

	# Append data
	x_vals.append(next(index))
	y_vals.append(data)

	# Fit data in window
	l = len(x_vals)
	if l > window:
		n = l-window
		del x_vals[:n]
		del y_vals[:n]

	# Plot
	plt.cla()
	plt.title("STM32 data")
	plt.xlabel("Time (sec)")
	plt.ylabel("Value")
	#plt.style.use("dark_background")
	plt.tight_layout()
	plt.legend(["Hello"])
	plt.plot(x_vals, y_vals)

for i in range(window):
	x_vals.append(next(index))
	y_vals.append(0)

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()
