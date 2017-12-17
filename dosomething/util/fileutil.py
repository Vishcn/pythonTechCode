# -*- coding: utf-8 -*-
'''
Created on 2011-01-14

@author: sixi
'''

import logutil
import os
import traceback

def mkdir(directory):
    if (not os.path.exists(directory)) or (not os.path.isdir(directory)):
        try:
            logutil.logger.logger.info('Create %s.' % directory)
            os.makedirs(directory)
        except:
            logutil.logger.logger.exception(traceback.format_exc())

def removeDirectory(directory):
    logutil.logger.logger.info('Clean %s.' % directory)
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(directory)
