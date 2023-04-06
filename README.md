# Reheating by Scalaron Decay

Python script to solve  inflationary and reheating phase for f(R) = R + alpha R^2 + beta R^2 ln (R/mu^2)

This gravity model gives an inflationary phase and a subsequent reheating phase due to particle creation at the expense of scalaron field. Presenting a plausible scenario of reheating obeying Heisenberg’s uncertainty principle that imposes constraints on the particles that can be created in the
configuration space. The energy available in the scalaron field is sufficient to populate the entire configuration space, the energy density of the particles grows, attaining a maximum value giving an efficient
reheating.

Source Code is separated into several python modules performing specific tasks:

1. Codes relating to inflation and reheating are scripted in two different python file placed in the source directory.Additional
source ‘fieldeqs.py’ include all model parameters, field equations and other associate quantities. A similar but different
f(R) model can be studied using the same code by modifying the ‘fieldeqs.py’ file accordingly.

2. In addition, the tools directory inside source directory include logger.py and plotter.py files. The ‘logger.py’ will
generate the log file when the code is executed and this file will help one to keep track of what has done previously.

The plotter.py include several plot functions that are called at different places in the source code to plot the result.

All the result can be found in the directory ‘op_data’.

-------------------------------------------------------------------------------------

### Developer

Arun Mathew, New Numerical Lab, Dept. of Physics, IIT Guwahati, India - 781039

------------------------------------------------------------------------------------

### License

[MIT](https://choosealicense.com/licenses/mit/)

-------------------------------------------------------------------------------------
