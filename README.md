# Reheating by Scalaron Decay

Python code for solving inflationary and reheating phase of f(R) gravity. Source Code is separated into 
several python modules performing specific tasks. 

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

-------------------------------------------------------------------------------------

### Documentation

For more detailed see the code documentation at 
https://arun-mathew-github.github.io/Scalaron_Reheating/
-------------------------------------------------------------------------------------

### Developer

Dr. Arun Mathew, New Numerical Lab, Dept. of Physics, IIT Guwahati, India - 781039
------------------------------------------------------------------------------------

### License
[MIT](https://choosealicense.com/licenses/mit/)
-------------------------------------------------------------------------------------
