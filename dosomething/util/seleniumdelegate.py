# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2011

@author: sixi
'''

import sys
import os

from util.logutil import logger

def startSeleniumServer(proxy_host = '', proxy_port = ''):
    path_list = os.getcwd().split(os.sep)[:-2]
    path_list.append('lib')
    path_list.append('selenium-remote-control-1.0.3')
    path_list.append('selenium-server-1.0.3')
    path = os.sep.join(path_list)
    cd_path_command = 'cd %s' % path
    
    server_command_option = ''
    if proxy_host != '' and proxy_port != '':
        server_command_option = '-Dhttp.proxyHost=%s -Dhttp.proxyPort=%s' % (proxy_host, proxy_port)
    server_command = 'java -jar selenium-server.jar %s&' % server_command_option
    
    command = '%s && %s' % (cd_path_command, server_command)

    logger.logger.debug(command)
    os.system(command)

def stopSeleniumServer():
    command = 'ps aux | grep selenium | grep -v grep | awk \'{print $2}\' | xargs kill'
    logger.logger.debug(command)
    os.system(command)

if __name__ == '__main__':
    startSeleniumServer()
#    stopSeleniumServer()
