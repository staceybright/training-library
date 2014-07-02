#! /usr/bin/env python

"""Monitors the hot pixel evolution of WFC3/UVIS darks.

This module serves as a simple yet practical example of a
calibration/monitoring script that one might write for work on an
instrument team (generally speaking).  Of course, if this script were
to be used as part of a real calibration, it would likely be expanded
and reconfigured to be more robust.  In addition, this module attempts
to use python 'best practices' that promote readabilty, consistency,
reusability, etc.  It uses PEP-8 standards, docstrings, and minimal
overlap as it attempts to be a D.R.Y. (Don't repeat yourself) code.
By no means should this style be used as a hard rule or guideline,
but rather a suggestion for producing high-level user-friendly python
code.

In this particular script, the number of hot pixels are counted in
WFC3/UVIS dark images and plotted over time.  The threshold for
determining which pixels are to be considered "hot" is given as a
command line argument.  Specifically, darks that were acquired between
2014-01-02 and 2014-02-26 are processed.  A WFC3/UVIS anneal occured on
2014-01-30, in which the detector was warmed to reduce the number of
hot pixels.  All data points are normalized to the anneal date.

Authors:
    Matthew Bourque, July 2014

Use:
    This script is inteded to be executed from the command line as
    such:

        >>> python dark_monitor.py

    The hot pixel threshold can be specified with the -t or --threshold
    argument.  For example:

        >>> python dark_monitor.py -t 8.5

    If no threshold is specified, the default value of 9.0 is used.

Outputs:

    hotpix.png -- A plot showing the number of hot pixels in each dark
                  as a function of MJD, placed in the current working
                  directory.

References:

    The Python RIAB Traning Document
    (https://confluence.stsci.edu/display/INSRIA/RIA+training)
"""

import argparse
from astropy.io import fits
import glob
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------

def get_percentage_hotpix(image, threshold):
    """Determine the observation date and number of hot pixels for the
    image.

    Parameters:
        image : string
            The path to the image to process.
        threshold : float
            The threshold above which pixels will be considered hot
            pixels.

    Returns:
        mjd : float
            The Modified Julian Date of the image.
        percentage_hotpix : float
            The percentage of hot pixels in SCI extension of the image.

    Outputs:
        nothing
    """

    # Open the file
    hdulist = fits.open(image)

    # Get data from the SCI and DQ extensions
    sci = hdulist[1].data
    dq = hdulist[3].data

    # Get the MJD of observation
    mjd = hdulist[0].header['EXPSTART']

    # Determine which pixels are hot pixels
    good_data = sci[np.where(dq == 0)]
    hotpix = good_data[np.where(good_data > threshold)]

    # Calculate the percentage of hot pixels
    num_pix = float(sci.size)
    num_hotpix = float(hotpix.size)
    percentage_hotpix = (num_hotpix / num_pix) * 100.

    return mjd, percentage_hotpix

# -----------------------------------------------------------------------------

def parse_args():
    """Parse command line arguments.

    Parameters:
        nothing

    Returns:
        args : argparse.Namespace object
            An argparse object containing all of the added arguments.

    Outputs:
        nothing
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-t --threshold',
        dest='threshold',
        action='store',
        type=float,
        required=False,
        help='Pixel value to be used as hot pixel threshold',
        default=9.0)
    args = parser.parse_args()

    return args

# -----------------------------------------------------------------------------

def plot_hot_pixels(threshold):
    """Plots WFC3/UVIS hot pixel evolution.

    Parameters:
        threshold : float
            The threshold above which pixels will be considered hot
            pixels.

    Returns:
        nothing

    Outputs:
        hotpix.png - A plot showing the number of hot pixels over time
    """

    # Set anneal date
    anneal = 56687.4698727

    # Initialize plot
    figure, ax = plt.subplots()
    ax.grid()
    ax.minorticks_on()
    ax.set_title('WFC3/UVIS Hot Pixel Evolution')
    ax.set_xlabel('Days from anneal')
    ax.set_ylabel('Number of Hot Pixels (% of Chip)')

    # Plot the anneal
    ax.axvline(x=0, c='r', ls='--', lw=2, label='Anneal')

    # Plot the percentage of hot pixels
    dark_files = glob.glob('/user/gunning/Python_Training/uvis_darks/*.fits')
    for dark_file in dark_files:

        print 'Processing {}'.format(dark_file)

        # Determine observation time and number of hot pixels
        time, hotpix = get_percentage_hotpix(dark_file, threshold)

        # Plot the # of hot pixels vs time
        ax.scatter(time - anneal, hotpix, s=50, c='k', marker='+')

    # Save figure
    ax.legend(loc='best')
    savefile = 'hotpix.png'
    plt.savefig(savefile)
    print 'Saved figure to {}'.format(savefile)

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    args = parse_args()
    plot_hot_pixels(args.threshold)
