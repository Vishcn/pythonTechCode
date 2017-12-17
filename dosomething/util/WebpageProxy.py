# -*- coding: utf-8 -*-

'''
Created on Jan 19, 2011

@author: sixi
'''

import datetime
import fileutil
import logutil
import os
import hashlib
import traceback
import time

url_access_max_count = 3

class WebpageProxy(object):
    '''
    classdocs
    '''

    def __init__(self, webpage_directory = 'webpage'):
        '''
        Constructor
        '''
        fileutil.mkdir(webpage_directory)
        self.webpage_directory = webpage_directory

    def getWebpage(self, url, selenium_obj):
        now_datetime = datetime.datetime.now()
        print now_datetime
        logutil.logger.logger.debug('Access to the URL: %s' % url)
        
#        count = 0
#        while True:
#            try:
#                selenium_obj.open(url)
#                break
#            except Exception, e:
#                count += 1
#                if count < url_access_max_count:
#                    logutil.logger.logger.exception(traceback.format_exc())
#                    continue
#                else:
#                    raise Exception('%d Exception in selenium opening.' % url_access_max_count)
        
        selenium_obj.open(url)
        time.sleep(10)
        content = selenium_obj.get_html_source()
        print content
        file_name = hashlib.md5(url).hexdigest()
        file_path = os.path.join(self.webpage_directory, file_name)
        logutil.logger.logger.debug('Write file %s' % file_path)
        webpage_file = open(file_path, 'w')
        webpage_file.write(content)
        webpage_file.close()
        return content

if __name__ == '__main__':
#    webpage_proxy = WebpageProxy()
#    webpage_proxy.getWebpage(None, None)
    print hashlib.md5('http://theater.mtime.com/China_Beijing/cinema/').hexdigest()
