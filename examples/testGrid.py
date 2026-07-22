from physical_optics.common.grid import Grid
import matplotlib.pyplot as plt

grid = Grid(512, 512, 5e-6, 5e-6)

plt.figure()
plt.plot(grid.x)
plt.title("x coordinate")

plt.figure()
plt.imshow(grid.X)
plt.colorbar()

plt.show()