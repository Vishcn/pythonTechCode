# -*- coding: utf-8 -*-

import re
import urllib2
import threading
import Queue
import traceback

class TestProxy(threading.Thread):
    '''
    Check the validation of the proxies using multi-thread.
    '''

    def __init__(self,
                 queue,
                 proxy_tested_list,
                 mutex,
                 test_url,
                 key_word):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.queue = queue
        self.proxy_tested_list = proxy_tested_list
        self.mutex = mutex
        self.test_url = test_url
        self.key_word = key_word

    def run(self):
        while True:
            try:
                proxy_address = self.queue.get(False)
                proxy_support = urllib2.ProxyHandler({'http':'http://' + proxy_address})
                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
                headers = {
#                 'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6'
                  'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.14) Gecko/20110218 Firefox/3.6.14',
#                 'Referer':'http://www.dianping.com/',
                  'X-Forwarded-For':'http://127.0.0.1'
                }
                req = urllib2.Request(
                    url = self.test_url,
                    headers = headers
                )
                print 'using', proxy_address, 'to request', self.test_url
                try:
                    page = urllib2.urlopen(req).read()
                    damaiSign = re.search(self.key_word, page)
                    if damaiSign:
                        print 'The proxy', proxy_address, 'is worked!'
                        self.mutex.acquire()
                        self.proxy_tested_list.append(proxy_address)
                        self.mutex.release()
                    else:
                        print 'The web page is not aim.'
                except:
                    continue
            except Queue.Empty:
                print 'The queue is empty.'
                return

if __name__ == '__main__':
    pass
#    TestProxy.TestProxy(proxy_queue, proxy_tested_list, mutex, test_url, key_word)
