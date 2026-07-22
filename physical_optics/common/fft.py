import numpy as np


def fft2c(U):
    """
    Centered two-dimensional Fourier transform.

    Parameters
    ----------
    U : ndarray
        Complex input field.

    Returns
    -------
    ndarray
        Centered Fourier transform.
    """

    return np.fft.fftshift(
        np.fft.fft2(
            np.fft.ifftshift(U)
        )
    )


def ifft2c(A):
    """
    Centered inverse two-dimensional Fourier transform.

    Parameters
    ----------
    A : ndarray
        Complex Fourier spectrum.

    Returns
    -------
    ndarray
        Centered inverse Fourier transform.
    """

    return np.fft.fftshift(
        np.fft.ifft2(
            np.fft.ifftshift(A)
        )
    )

def fftc(u):
    """Centered one-dimensional Fourier transform."""

    return np.fft.fftshift(
        np.fft.fft(
            np.fft.ifftshift(u)
        )
    )


def ifftc(a):
    """Centered inverse one-dimensional Fourier transform."""

    return np.fft.fftshift(
        np.fft.ifft(
            np.fft.ifftshift(a)
        )
    )