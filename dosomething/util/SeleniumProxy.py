'''
Created on Jan 18, 2011

@author: sixi
'''

import random
import os
import fileutil
from selenium import selenium
from logutil import logger

class SeleniumProxy(object):
    '''
    classdocs
    '''

    def __init__(self, proxy_list = 'proxy_list'):
        '''
        Constructor
        '''
        logger.logger.info('Initialization of SeleniumProxy by proxy_list = %s.' % proxy_list)
        proxy_file = file(proxy_list, "r")
        self.proxy = (proxy_file.read())[:-1].split('\n')
        self.index = random.randint(0, len(self.proxy) - 1)
    
    def createFirefoxPrefDirectory(self, server_port, proxy_host, proxy_port, firefox_pref_directory):
        pref_directory = os.path.join(firefox_pref_directory, str(server_port))
        fileutil.mkdir(pref_directory)
        pref_file_path = os.path.join(pref_directory, 'prefs.js')
        pref_file = open(pref_file_path, 'w')
        pref_file.write('user_pref("network.http.proxy.version", "1.0");\n')
        pref_file.write('user_pref("network.proxy.no_proxies_on", "localhost");\n')
        pref_file.write('user_pref("network.proxy.http", "%s");\n' % proxy_host)
        pref_file.write('user_pref("network.proxy.http_port", %d);\n' % proxy_port)
        pref_file.write('user_pref("network.proxy.type", 1);\n')
        pref_file.close()
        return pref_directory

    def startSeleniumServer(self, server_port = 4444, proxy_host = '', proxy_port = '', firefox_pref_directory = 'firefox_profiles'):
        path_list = os.getcwd().split(os.sep)[:-2]
        path_list.append('lib')
        path_list.append('selenium-remote-control-1.0.3')
        path_list.append('selenium-server-1.0.3')
        path_list.append('selenium-server.jar')
        jar_path = os.sep.join(path_list)
        
        if proxy_host == '' or proxy_port == '':
            server_command = 'java -jar %s -port %d &' % (jar_path, server_port)
        else:
            pref_directory = self.createFirefoxPrefDirectory(server_port, proxy_host, proxy_port, firefox_pref_directory)
            server_command = 'java -jar %s -port %d -firefoxProfileTemplate %s &' % (jar_path, server_port, pref_directory)
        
        logger.logger.debug(server_command)
        os.system(server_command)

    def stopAllSeleniumServer(self):
        command = 'ps aux | grep selenium | grep -v grep | awk \'{print $2}\' | xargs kill'
        logger.logger.debug(command)
        os.system(command)

    def stopSeleniumServer(self, server_port = 4444):
        command = 'ps aux | grep selenium | grep -v grep | grep \'port %d\' | awk \'{print $2}\' | xargs kill' % server_port
        logger.logger.debug(command)
        os.system(command)

    def getSelenium(self, port = 4444, url = 'http://www.google.com.hk'):
        seleniumObj = selenium('localhost', port, '*firefox', url)
        seleniumObj.start()
        return seleniumObj

if __name__ == '__main__':
    selenium_test_obj = SeleniumProxy()
    selenium_test_obj.createFirefoxPrefDirectory(4444, '203.192.6.100', 80, 'firefox_profiles')
