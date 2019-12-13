# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:37:51 2019

@author: George Ciesinski
"""

import logging
from logging import handlers
from Gui import Gui
from ImageProcessor import ImageProcessor

        
"""
Basic setup and class initialization
"""

# Logger Setup
# TODO: Create several logs to track past several attempts to use app (5 - 10 tops)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s -%(levelname)s : %(message)s')
# file_handler = logging.FileHandler('Logs/logs.log')
file_handler = handlers.RotatingFileHandler('Logs/logs.log', mode='w', backupCount=5)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Creates a new log file every time program is ran 
file_handler.doRollover()

# Starts the image processor
ip = ImageProcessor(logger)

# Create GUI object
g = Gui(ip, logger)

# Put up welcome image, includes GUI instance
ip.welcome_image(g)

# Tkinter main loop
g.root.mainloop()
