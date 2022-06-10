# Setting up Console and File Logger
# Author: Arun Mathew
# Last modification: 22 May 2022

import logging

def setup_logger(FileName):

    #####################################################################################
    #####################################################################################
    # Create a logger:
    # First we need to create a logger, which is nothing but an object to the logger
    # class. We can create this by using getLogger(). Logger
    # object we have to set the log level using setLevel() method.
    logger = logging.getLogger(FileName)
    logger.setLevel(logging.DEBUG)


    #####################################################################################
    #####################################################################################
    # Handler:
    # Create a handler object and set the logging level.
    # 1. Stream Handler to log messages to the console.
    # 2. File Handler to log messages to a log file.

    # Stream Handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    # File Handler
    fileHandler = logging.FileHandler('scalaron_decay.log')
    fileHandler.setLevel(logging.DEBUG)


    #####################################################################################
    #####################################################################################
    # Create Formatter:
    formatter = logging.Formatter('%(asctime)s – [%(name)s:%(lineno)d] – %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')


    #####################################################################################
    #####################################################################################
    # Add Formatter to Console Handler and File Handler
    consoleHandler.setFormatter(Custom_Formatter())
    fileHandler.setFormatter(formatter)


    #####################################################################################
    #####################################################################################
    # Add Handler object to the Logger
    # Then the handler object should be added to the logger object using addHandler()
    # method.
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger



#####################################################################################
#####################################################################################
# Color text for log message
class Custom_Formatter(logging.Formatter):
    green = '\033[92m'
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - [%(name)s: %(lineno)d] - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }


    #####################################################################################
    #####################################################################################
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
