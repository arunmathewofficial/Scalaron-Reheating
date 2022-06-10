# Setting up class file for the region of Reheating
# Author: Arun Mathew

from fieldeqs import *

#####################################################################################
# > Set the logger tree-level
SDlogger = logger.setup_logger('Reheating')

class reheating():

    def __init__(self):
        print('reheating')