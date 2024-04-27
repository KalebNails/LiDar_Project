import matplotlib.pyplot as plt
import json
import math

with open("combinedoutput.json",'r') as file:
	data =json.load(file)
print(data)
print(len(data["angle"]))
print(len(data["distance"]))

plt.figure()
#ax = plt.subplot(111,projection='polar')
#ax.plot(data["distance"],data["angle"])

# Convert angles from degrees to radians
angles_radians = [math.radians(angle) for angle in data["angle"]]

# Calculate Cartesian coordinates (x, y)
x_coords = [distance * math.cos(angle) for angle, distance in zip(angles_radians, data["distance"])]
y_coords = [distance * math.sin(angle) for angle, distance in zip(angles_radians, data["distance"])]
plt.plot(x_coords, y_coords, marker='o', markersize=2, linestyle='None')

plt.grid(True)

#plt.polar(data["angle"],data["distance"],marker ='o',markersize = 2, linestyle='None')
plt.show()


