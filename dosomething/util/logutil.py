# -*- coding: utf-8 -*-

'''
Created on 2010-8-20

@author: sixi
'''

import datetime
import logging
import logging.handlers
import os
import fileutil

def log(log_message, log_file = 'log.txt', terminator_print = False):
#    if terminator_print:
#        try:
#            print log_message
#        except:
#            print 'An exception occured when print log message.'
    bug_file = file(log_file, 'a')
    date_time = datetime.datetime.now()
    bug_file.write(date_time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    bug_file.write(log_message + '\n')
    bug_file.close()

def write(message, aim_file):
    aim_file = file(aim_file, 'a')
    aim_file.write(message)
    aim_file.close()

class logger(object):

    def __init__(self, name = 'root', log_level = logging.DEBUG, log_filename = os.path.join('log', 'log.txt'), maxBytes = 1000000, backupCount = 5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        log_directory = os.sep.join(log_filename.split(os.sep)[:-1])
        
        if (not os.path.exists(log_directory)) or (not os.path.isdir(log_directory)):
            os.makedirs(log_directory)

        handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes = maxBytes, backupCount = backupCount)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(lineno)d %(module)s %(funcName)s %(message)s')
    
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def settings(self, name = 'root', log_level = logging.DEBUG, log_filename = os.path.join('log', 'log.txt'), maxBytes = 1000000, backupCount = 5):
        self.__init__(name, log_level, log_filename, maxBytes, backupCount)

logger = logger()

if __name__ == '__main__':
    logger.logger.critical('This is a critical.')
    logger.logger.debug('This is a debug.')
    logger.logger.info('This is a info.')
    logger.logger.error('This is an error.')
    logger.logger.exception('This is an exception.')
