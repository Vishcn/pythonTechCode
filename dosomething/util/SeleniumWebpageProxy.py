'''
Created on Jan 22, 2011

@author: sixi
'''

import SeleniumProxy
import WebpageProxy
import proxy
import time
import logutil
import traceback

class SeleniumWebpageProxy(object):
    '''
    classdocs
    '''

    def __init__(
      self,
      selenium_proxy = SeleniumProxy.SeleniumProxy(),
      webpage_proxy = WebpageProxy.WebpageProxy(),
      proxy_class = proxy.Proxy(),
      server_port = 4444,
      pref_directory = 'firefox_profiles'
    ):
        '''
        Constructor
        '''
        self.selenium_proxy = selenium_proxy
        self.webpage_proxy = webpage_proxy
        self.proxy_class = proxy_class
        self.server_port = server_port
        self.pref_directory = pref_directory
        self.selenium_entity = None

    def openViaProxy(self, url, timeout = 600000):
        while True:
            try:
                self.proxy_class.nextproxy()
                ip, port = self.proxy_class.getproxyIPandPort()
                
                # need polishing
                self.selenium_proxy.stopSeleniumServer(self.server_port)
                
                self.selenium_proxy.startSeleniumServer(self.server_port, ip, int(port), self.pref_directory)
                time.sleep(10)
                self.selenium_entity = self.selenium_proxy.getSelenium(self.server_port, url)
                self.selenium_entity.set_timeout(timeout)
#                self.selenium_entity.wait_for_page_to_load(timeout)
                content = self.webpage_proxy.getWebpage(url, self.selenium_entity)
                return content
            except:
                logutil.logger.logger.exception(traceback.format_exc())
                pass

    def openViaNoProxy(self, url, timeout = 600000):
        self.selenium_proxy.stopSeleniumServer(self.server_port)
        self.selenium_proxy.startSeleniumServer(self.server_port)
        time.sleep(10)
        self.selenium_entity = self.selenium_proxy.getSelenium(self.server_port, url)
        self.selenium_entity.set_timeout(timeout)
        content = self.webpage_proxy.getWebpage(url, self.selenium_entity)
        return content

    def open(self, url, proxy = 'continue', timeout = 600000):
        if proxy == 'continue':
            if self.selenium_entity == None:
                content = self.openViaProxy(url, timeout)
            else:
                try:
                    content = self.webpage_proxy.getWebpage(url, self.selenium_entity)
                except:
                    content = self.openViaProxy(url, timeout)
        elif proxy == 'change':
            content = self.openViaProxy(url, timeout)
        elif proxy == 'no_proxy':
            content = self.openViaNoProxy(url, timeout)
        
        return content
