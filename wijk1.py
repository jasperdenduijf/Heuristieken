import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png

# make a subplot to allow for add_artist
ax = plt.subplot(111)

# get the house image
house = read_png('house.png')
houseimg = OffsetImage(house, zoom=.1)

# get the house coordinates
xy=[]

with open('wijk1_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if row[0] != "x":
			xy.append([int(row[0]), int(row[1])])

# add the house image to the coordinates
for row in xy:
	ab = AnnotationBbox(houseimg, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points")                                  
	ax.add_artist(ab)

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.axis([0, 50, 0, 50])
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 10, 20, 30, 40, 50])

# show the plot
plt.show()