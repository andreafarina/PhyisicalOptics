import numpy as np


class Field:
    """
    Scalar optical field.

    Parameters
    ----------
    grid : Grid
        Spatial grid.
    wavelength : float
        Wavelength [m].
    """

    def __init__(self, grid, wavelength):

        if wavelength <= 0:
            raise ValueError("Wavelength must be positive.")

        self.grid = grid
        self.wavelength = wavelength
        self.k = 2 * np.pi / wavelength

        # Complex field
        self.U = np.ones((grid.Ny, grid.Nx), dtype=complex)