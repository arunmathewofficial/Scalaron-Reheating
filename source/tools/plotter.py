# Setting up Plotter function
# Author: Arun Mathew
# Last modification: 22 May 2022

import matplotlib.pyplot as plt
import os
from itertools import islice
import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
#mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']


#####################################################################################
def plot_single(x,
            y,
            x_range,
            y_range,
            x_label,
            y_label,
            filename,
            filetype):
    '''
    This function plots f(x) as the function of x

    :param x: x values
    :param y: y values
    :param x_range: plot range along x axis
    :param y_range: plot range along y axis
    :param x_label: x label
    :param y_label: y label
    :param filename: output filename
    :param filetype: specify filetype as string
    :return: None
    '''


    fig, ax = plt.subplots(figsize=(4.5, 3), dpi=100)

    ax.plot(x, y)
    plt.xlim(x_range)
    plt.ylim(y_range)

    ax.set_xlabel(x_label, color="black", fontsize=20)
    plt.ylabel(y_label, color="black", fontsize=20)


    #plt.legend()
    plt.tight_layout()

    # Path of data directory
    root_Dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    data_Dir = root_Dir + "/op_data"

    fig.savefig(data_Dir + '/' + filename + '.' + filetype)
    plt.show()


#####################################################################################
def plot_multiple(x,
            y,
            x_range,
            y_range,
            x_label,
            y_label,
            filename):


    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.xlim(x_range)
    plt.ylim(y_range)

    ax.set(xlabel = x_label, ylabel = y_label, title='')

    plt.legend()
    plt.tight_layout()

    fig.savefig(filename + '.png')
    plt.show()