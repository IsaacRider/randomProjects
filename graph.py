import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,5])
y = np.array([1,2,4,6])

plt.subplot(3,2,1)
plt.plot(x,y,"o k", ms = "10")
plt.suptitle("Big Title", fontproperties = "Times New Roman")
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.tick_params(axis='both', which='major', labelsize=10, labelfontfamily = "Times New Roman")
plt.ylabel("Y Axis", fontproperties = "Times New Roman")
plt.xlabel("X Axis", fontproperties = "Times New Roman")
plt.grid(color = "black", linewidth = "3")

x = np.array([3,7,46,25,64,75,23,67,85,245])
y = np.array([2,3,42,34,23,53,75,23,97,202])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70])

plt.subplot(3,2,2) # Columns, Rows, Order
plt.scatter(x, y, c = colors, cmap = 'viridis')
plt.colorbar()
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.tick_params(axis='both', which='major', labelsize=10, labelfontfamily = "Times New Roman")
plt.ylabel("Y Axis", fontproperties = "Times New Roman")
plt.xlabel("X Axis", fontproperties = "Times New Roman")
plt.grid(color = "black", linewidth = "2")

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.subplot(3,2,3)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.tick_params(axis='both', which='major', labelsize=10, labelfontfamily = "Times New Roman")
plt.ylabel("Y Axis", fontproperties = "Times New Roman")
plt.xlabel("X Axis", fontproperties = "Times New Roman")

x = np.array(["A", "D", "C", "R", "O"])
y = np.array([1,2,3,4,6])

plt.subplot(3,2,4)
plt.bar(x,y, color = "black", width = 2)
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.tick_params(axis='both', which='major', labelsize=10, labelfontfamily = "Times New Roman")
plt.ylabel("Y Axis", fontproperties = "Times New Roman")
plt.xlabel("X Axis", fontproperties = "Times New Roman")

# A histogram is a graph showing frequency distributions.

y = np.array([1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,6,6,6,6,7,8,6,5,6,6,4,3,2,4,9,40])

plt.subplot(3,2,5)
plt.hist(y, color = "black", width = 1)
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.title("Title", fontproperties = "Times New Roman", loc = "left")
plt.ylabel("Y Axis", fontproperties = "Times New Roman")
plt.xlabel("X Axis", fontproperties = "Times New Roman")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.subplot(3,2,6)
plt.pie(y, labels = mylabels)

plt.show()