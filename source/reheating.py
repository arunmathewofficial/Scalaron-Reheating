# Setting up class file for the region of Reheating
# Author: Arun Mathew

from fieldeqs import *
from scipy.integrate import solve_ivp
from tools import plotter

#####################################################################################
# > Set the logger tree-level
SDlogger = logger.setup_logger('Reheating')

class reheating():
    '''
    sda
    '''

    def __init__(self, model_object, REH_IC, output_file):
        SDlogger.info('Setting up initial attributes for Reheating.')
        self.model_object = model_object  # create a object for the class model
        # Initial Conditions for Inflation
        self.REH_IC = REH_IC
        SDlogger.info('Reheating - Initial Conditions : [%f,%f,%f,%f].',
                      self.REH_IC[0], # Initial Reheating time
                      self.REH_IC[1], # Initial Reheating Hubble rate (in the units of H0)
                      self.REH_IC[2], # Initial Reheating Hubble slope (in the unit of H0t0)
                      self.REH_IC[3]  # Initial Reheating Density in the units of E^4
                      )

        # Reheating Time vector
        start_time = self.REH_IC[0]
        self.t_scale = model_object.timescales()[1]
        end_time = model_object.timescales()[1] * 5000
        step_size = model_object.timescales()[1] / 100
        num_steps = int((end_time - start_time) / step_size)
        self.tvector = numpy.linspace(start=start_time, stop=end_time, num=num_steps)
        self.tspan = [start_time, end_time]
        # Name of output data file
        self.output_file = output_file


    def reheating_solver(self):
        """
        Solve inflation field equations for the region of inflation

        The docstring in the function should fully explain what the function is
        for and how to use it

                        * this is a bullet list
                        * with multiple entries and some text in *italic* and even **bold**.
                          The bullet list items can span multiple lines which are indented

                        .. warning:: bullet (as well as enumerated) lists have to start and end
                           with an empty line

                        1. Single backquotes are for **references** to other documented items.
                           For example `basf2.Module` will link to the documentation of the class
                           Module in the python module basf2. A different link name and link
                           target can be specified with <>: `Module class <basf2.Module>` will
                           link to basf2.Module but the link will read "Module class"
                        2. Double backquotes are for ``literal text``.

                        .. warning:: this is different to markdown where single backquotes are
                           usually used for literal text

                        3. Links to external websites are usually of the form `Link Text <http://example.com>`_.

                        .. note:: there is an underscore at the end of links

                        4. math is supported either inline :math:`f(x) = \sum_{x=i}^N x^i` or as
                           display verssion:

                           .. math::

                              f(x) = \sum_{i=1}^N x^i

                           .. seealso:: `Math support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/math.html>`_
                        5. The easiest way for code example is the "doctest" syntax: Start a new
                           paragaph after an empty line with ``>>>`` followed by the python
                           statements and (optionally) the expected output of these statements.

                           >>> dummy_function_example("some name", foo="bar")
                           "Hello some name, Lord of bar"

                           .. seealso:: `Showing code examples <http://www.sphinx-doc.org/en/stable/markup/code.html>`_

                        6. To document parameters and return types please use the :ref:`googlestyle` as shown below:

                        Note:
                          For class members please do not include the ``self`` parameter in this list

                        Parameters:
                          name (str): Description of the first parameter
                           Can also span multiple lines if indented properly
                          foo: Second parameter but no type given

                        Returns:
                          inf_tspan (1D array): time span of inflation in the unit of t_Planck

                          Xi,
                          Psi,
                          The,
                          Ricci,
                          Epsilon_1,
                          Epsilon_3,
                          Epsilon_4,
                          n_s,
                          r,
                          Status_flag

                        See Also:
                          Some references to other functions

        """
        t_points = self.tvector
        IC = [self.REH_IC[1], self.REH_IC[2], self.REH_IC[3]]
        tspan = self.tspan

        sol = solve_ivp(self.model_object.field_eqs, tspan, IC, t_eval=t_points,
                        method='LSODA', atol=1e-16, rtol=2.3e-14
                        #events=[self.stop_condition, ]  # Stopping Condition for integration
                        )

        reh_tspan = sol.t

        Xi  = sol.y[0]
        Psi = sol.y[1]
        The = sol.y[2]


        plotter.plot_single(reh_tspan/self.t_scale, Xi, [1,10], [0, 0.04], '$t/t_{osc}$', '$\\xi$', 'reh_initial_H', 'png')
        plotter.plot_single(reh_tspan/self.t_scale, The, [1, 10], [0, 0.0004], '$t/t_{osc}$', '$\\rho/\epsilon^4$', 'reh_initial_rho', 'png')

        plotter.plot_single(reh_tspan / self.t_scale, Xi, [1, 5000], [0, 0.04], '$t/t_{osc}$', '$\\xi$', 'reh_full_H', 'png')
        plotter.plot_single(reh_tspan / self.t_scale, The, [1, 5000], [0, 0.4], '$t/t_{osc}$', '$\\rho/\epsilon^4$','reh_full_rho', 'png')
