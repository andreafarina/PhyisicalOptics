from physical_optics.common.grid import Grid
from physical_optics.common.field import Field

from physical_optics.objects.apertures import (
    circular_aperture,
    rectangular_aperture,
)

from physical_optics.visualization.plot import show_intensity

import matplotlib.pyplot as plt


# Grid
grid = Grid(512, 512, 5e-6, 5e-6)

# Optical field
field = Field(grid, 633e-9)

# Apply an aperture
#field.U *= circular_aperture(grid, radius=500e-6)
field.U *= rectangular_aperture(
    grid,
    width=400e-6,
    height=800e-6,
)

# Display
show_intensity(field)
plt.show()