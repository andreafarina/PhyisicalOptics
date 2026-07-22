

import numpy as np


"""
Functions to generate the transmission of ideal optical lenses.

Each function returns the complex transmission evaluated on the
provided Grid.
"""


def thin_lens(grid, wavelength, focal_length):
    """
    Thin lens.

    Parameters
    ----------
    grid : Grid
        Spatial grid.
    wavelength : float
        Wavelength [m].
    focal_length : float
        Lens focal length [m].

    Returns
    -------
    ndarray
        Complex lens transmission.
    """

    if wavelength <= 0:
        raise ValueError("Wavelength must be positive.")

    if focal_length == 0:
        raise ValueError("Focal length cannot be zero.")

    k = 2 * np.pi / wavelength

    phase = -(k / (2 * focal_length)) * (grid.X**2 + grid.Y**2)

    return np.exp(1j * phase)