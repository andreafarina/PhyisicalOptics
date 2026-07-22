

import numpy as np


"""
Functions to generate the transmission of ideal optical apertures.

Each function returns the aperture transmission evaluated on the
provided Grid.
"""


def slit(grid, width, x0=0.0):
    """
    One-dimensional slit.

    Parameters
    ----------
    grid : Grid
        Spatial grid.
    width : float
        Slit width [m].
    x0 : float, optional
        Slit center along x [m]. Default is 0.

    Returns
    -------
    ndarray
        Aperture transmission.
    """

    return (np.abs(grid.X - x0) <= width / 2).astype(float)



def rectangular_aperture(grid, width, height, x0=0.0, y0=0.0):
    """
    Rectangular aperture.

    Parameters
    ----------
    grid : Grid
        Spatial grid.
    width : float
        Aperture width along x [m].
    height : float
        Aperture height along y [m].
    x0 : float, optional
        Aperture center along x [m]. Default is 0.
    y0 : float, optional
        Aperture center along y [m]. Default is 0.

    Returns
    -------
    ndarray
        Aperture transmission.
    """

    return (
        (np.abs(grid.X - x0) <= width / 2)
        &
        (np.abs(grid.Y - y0) <= height / 2)
    ).astype(float)



def circular_aperture(grid, radius, x0=0.0, y0=0.0):
    """
    Circular aperture.

    Parameters
    ----------
    grid : Grid
        Spatial grid.
    radius : float
        Aperture radius [m].
    x0 : float, optional
        Aperture center along x [m]. Default is 0.
    y0 : float, optional
        Aperture center along y [m]. Default is 0.

    Returns
    -------
    ndarray
        Aperture transmission.
    """

    return (
        (grid.X - x0) ** 2 + (grid.Y - y0) ** 2 <= radius ** 2
    ).astype(float)