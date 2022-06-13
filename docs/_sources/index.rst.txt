.. Reheating by Scalaron Decay documentation master file, created by
   sphinx-quickstart on Fri Jun 10 15:58:27 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Reheating by Scalaron Decay's documentation!
=======================================================

Python code for solving inflationary and reheating phase for
:math:`f(R) = R + {\alpha} R^2 + {\beta} R^2 {\ln} \frac{R}{{\mu}^2}` gravity.

This gravity model gives an inflationary phase and a subsequent reheating phase due to particle
creation at the expense of scalaron field. Presenting a plausible scenario of reheating obeying
Heisenberg's uncertainty principle that imposes constraints on the particles that can be created in the
configuration space. The energy available in the scalaron field is sufficient to populate the entire
configuration space, the energy density of the particles grows, attaining a maximum value giving an efficient
reheating.

Source Code is separated into several python modules performing specific tasks.

The f(R) model under consideration gives an inflationary phase and a subsequent reheating phase by the decay of scalarons.
Codes relating to inflation and reheating are scripted in two different python file placed in the source directory. Additional
source 'fieldeqs.py' include all model parameters, field equations and other associate quantities. A similar but different
f(R) model can be studied using the same code by modifying the 'fieldeqs.py' file accordingly.

In addition, the tools directory inside source directory include logger.py and plotter.py files. The 'logger.py' will
generate the log file when the code is executed and this file will help one to keep track of what has done previously.
The plotter.py include several plot functions that are called at different places in the source code to plot the result.

All the result can be found in the directory 'op_data'. If this directory is not found then the code may pass error.
Before running the code, mkdir op_data at the root directory.

You make also find sphinx directory at the root. This directory is the build directory for sphinx documentation.

The docs include the documentation html files for the github pages.



.. _Introduction
.. toctree::
   :maxdepth: 2
   :caption: Informations

   info

.. toctree::
   :maxdepth: 2
   :caption: Code Documentation

   modules

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`