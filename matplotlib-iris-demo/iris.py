#!/usr/bin/env python


import re

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


datafile = './res/iris.data'


def get_data():
    """Retrieves the data from the file specified in 'datafile' and returns
    the it. Lines in 'datafile' have to have either of the following forms:

      1. '<float>, <float>, <float>, <anything>'

      2. '<integer>, <integer>, <integer>, <anything>'

      '<anything>' is cut out and remains unobserved.

    Returns a two-dimensional NumPy array containing the data values
    specified in 'datafile'.
    """
    data_list = []
    with open(datafile, 'r') as f:
        for line in f:
            data_list.append(np.asarray(
                    [float(i) for i in re.split(',',line)[0:-1]]))
    data = np.asarray(data_list)
    print data.ndim
    return data

def plot(data, show=True, save=False, filename='plot.png'):
    """Plots a NumPy array as a line graph and shows it in a new window or
    /and writes it to a file.

    data: NumPy array representing the data to be plotted.
    show: Boolean value indicating if the plot should immediately be shown
          in a new window.
    save: Boolean value indicating if the plot should be written to a file.
    filename: String name fo the file to write the plot to. Accepts common
              image file extensions. Requires 'save' to be True.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data)
    if show:
        plt.show()
    if save:
        plt.savefig(filename)


if __name__ == '__main__':
    data = get_data()
    # plot(data, show=False, save=True)
    plot(data)
