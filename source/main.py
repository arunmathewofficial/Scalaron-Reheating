# Mian file
# Author: Arun Mathew

from fieldeqs import *
from inflation import inflation
from reheating import reheating
import os

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)


# > Set the logger tree-level
SDlogger = logger.setup_logger('Main')

# > Set the operation mode
#Setting = 'Default'
# Under the Default Setting, the code is executed with the appropriate
# initial condition and physically plausible parameters.
Setting = 'Parameter space Sketch with varying beta'
# Under this setting, we follow the reference https://doi.org/10.1103/PhysRevD.32.2511.
# Plausible values of alpha is determined subjected to the constraint coming from
# the observation of Scalar Spectral Index and Tensor-to-Scalar ratio.
SDlogger.info('Operating mode : %s', Setting)


#################################################################################
if(Setting == 'Default'):
    # Region: Inflation
    # In this section, the code perform under the Default Setting
    # Default setting implies normal operation with single initial condition
    # and
    # Initializing model parameter
    SDlogger.info('Initializing model parameters')
    f_R_gravity = model(
        16.5*pow(t_P, 2),         # value of the parameter alpha
        0.3 * pow(t_P, 2),        # value of the parameter beta
        pow(10, -4)*pow(t_P,-1),  # value of the parameter mu
        pow(10, 13),              # Energy of the particles created
        1/3                       # Equation of State P = omega rho
    )

    # Initialize the class inflation
    INF = inflation(f_R_gravity,  # Inherit the class model using object f_R_gravity
                    "inf_data"  # Output file name
                    )
    # Solve inflation field equations and return
    INF_Register = INF.inflation_solver()

    INF_EndTime = INF_Register[0][-1]
    INF_EndXi = INF_Register[1][-1]
    INF_EndPsi = INF_Register[2][-1]
    INF_EndThe = INF_Register[3][-1]


#####################################################################################
if(Setting == 'Parameter space Sketch with varying alpha'):
    # Region: Inflation
    # Several Scalar Spectral Index and Tensor-to-Scalar ratio are obtained by varying
    # the parameter alpha for fixed value of beta and mu.
    # Taking beta value 0.3 tp^2 and mu value corresponding to the GUT energy scale,
    # see reference https://doi.org/10.1103/PhysRevD.32.2511.


    # Make parameter output data file in data directory
    root_Dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    data_Dir = root_Dir + "/op_data"
    filename = 'alpha_para_space'
    filetype = "txt"

    # Write data to text file
    SDlogger.info('Writting inflation data to filename : %s.', filename)
    with open(data_Dir + "/" + filename + "." + filetype, "w") as para_file:
        para_file.write("Project Title: Reheating by Scalaron Decay\n")
        para_file.write("File Type: Data \n")
        para_file.write("Author: Arun Mathew\n")
        para_file.write("Affiliation: Dept. of Physics, IIT Guwahati, India\n\n")
        para_file.write("Data: Parameter Space\n\n")
        para_file.write("alpha, beta, mu, n_s, r\n")

        # Parameter values
        SDlogger.info('Initializing model parameters')
        # Values of model parameters are given below with the value of the
        # parameter alpha generating by the for loop
        beta  = 0.3*pow(t_P, 2)             # value of the parameter beta
        mu    = pow(10,-4) * pow(t_P, -1)   # value of the parameter mu
        E     = pow(10, 13)                 # Energy of the particles created
        omega = 1/3                         # Equation of State P = omega rho

        count = 0
        for i in range(1, 100, 1):
            count += 1
            # for loop will generate the value of the parameter alpha
            alpha = (1 + i/4)*pow(t_P, 2)
            f_R_gravity = model(alpha, beta, mu, E, omega)

            # Initialize the class inflation
            INF = inflation(f_R_gravity,  # Inherit the class model using object f_R_gravity
                            "None"        # No output file
                            )
            # Solve inflation field equations and return end values
            Time, Xi, Psi, The, Ricci, Epsilon_1, Epsilon_3, Epsilon_4, n_s, r, Status = INF.inflation_solver()
            SDlogger.info('Iteration index: %d -- Status : [%s]', count, Status)
            # Save data to file
            # We choose appropriate alpha value that gives the observed Scalar Spectral
            # Index and Tensor-to-Scalar ratio.
            numpy.savetxt(para_file, numpy.c_[alpha/pow(t_P, 2), beta/pow(t_P, 2), mu/pow(t_P, -1), n_s, r], fmt="%f")


#####################################################################################
if(Setting == 'Parameter space Sketch with varying beta'):
    # Region: Inflation
    # Several Scalar Spectral Index and Tensor-to-Scalar ratio are obtained by varying
    # the parameter alpha for fixed value of beta and mu.
    # Taking beta value 0.3 tp^2 and mu value corresponding to the GUT energy scale,
    # see reference https://doi.org/10.1103/PhysRevD.32.2511.


    # Make parameter output data file in data directory
    root_Dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    data_Dir = root_Dir + "/op_data"
    filename = 'beta_para_space'
    filetype = "txt"

    # Write data to text file
    SDlogger.info('Writting inflation data to filename : %s.', filename)
    with open(data_Dir + "/" + filename + "." + filetype, "w") as para_file:
        para_file.write("Project Title: Reheating by Scalaron Decay\n")
        para_file.write("File Type: Data \n")
        para_file.write("Author: Arun Mathew\n")
        para_file.write("Affiliation: Dept. of Physics, IIT Guwahati, India\n\n")
        para_file.write("Data: Parameter Space with varying beta\n\n")
        para_file.write("alpha, beta, mu, n_s, r\n")

        # Parameter values
        SDlogger.info('Initializing model parameters')
        # Values of model parameters are given below with the value of the
        # parameter alpha generating by the for loop
        alpha = 2.572*pow(10,8)*pow(t_P, 2) # value of the parameter beta
        mu    = pow(10,-4) * pow(t_P, -1)   # value of the parameter mu
        E     = pow(10, 13)                 # Energy of the particles created
        omega = 1/3                         # Equation of State P = omega rho

        count = 0
        for i in range(1, 100, 1):
            count += 1
            # for loop will generate the value of the parameter alpha
            beta = (1 + i/4)*pow(10,6)*pow(t_P, 2)
            f_R_gravity = model(alpha, beta, mu, E, omega)

            # Initialize the class inflation
            INF = inflation(f_R_gravity,  # Inherit the class model using object f_R_gravity
                            "None"        # No output file
                            )
            # Solve inflation field equations and return end values
            Time, Xi, Psi, The, Ricci, Epsilon_1, Epsilon_3, Epsilon_4, n_s, r, Status = INF.inflation_solver()
            SDlogger.info('Iteration index: %d -- Status : [%s]', count, Status)
            # Save data to file
            # We choose appropriate alpha value that gives the observed Scalar Spectral
            # Index and Tensor-to-Scalar ratio.
            numpy.savetxt(para_file, numpy.c_[alpha/pow(t_P, 2), beta/pow(t_P, 2), mu/pow(t_P, -1), n_s, r], fmt="%f")


#####################################################################################
if(Setting == 'Default'):
    # Region :Reheating

    REH_IC = [INF_EndTime,
              INF_EndXi,
              INF_EndPsi,
              INF_EndThe
              ]
    REH = reheating(f_R_gravity,
                    REH_IC,
                    "reh_data"
                    )

    # Solve reheating field equations and return
    REH_Register = REH.reheating_solver()


