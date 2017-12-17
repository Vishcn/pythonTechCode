# -*- coding: utf-8 -*-

import urllib
import re
import socket
import threading
import Queue

import TestProxy
import logutil

# personal settings
rawProxyListFileName = 'proxy_list'
test_url = 'http://www.dianping.com/'
key_word = r'点评'

urlProxySrc = "http://www.proxycn.com/html_proxy/http-%d.html"
#urlProxySrc = 'http://www.proxycn.com/html_proxy/countryBJ-%d.html'
urlCnProxySrc = 'http://www.cnproxy.com/proxy%d.html'

proxy_number_per_page = 100
default_proxy_count = 50
socket.setdefaulttimeout(30)

def setTestOption(new_test_url, new_key_word):
    logutil.logger.logger.info(new_test_url + ' ' + new_key_word)
    global test_url
    test_url = new_test_url
    global key_word
    key_word = new_key_word

def getCheckedProxyListFromFile():
    print 'Begin to check the proxy list from file.'
    proxy_list = []
    try:
        file = open(rawProxyListFileName, 'r')
        proxy_list_from_file = file.read().split('\n')
        file.close()
        return testProxyViaMultiThread(proxy_list_from_file)
    except:
        pass
    return proxy_list

def getCheckedProxyListFromWeb(page_access_number):
    page_url = urlProxySrc % page_access_number
    print 'Begin to check the proxy list from web %s.' % page_url
    try_count = 0
    while try_count < 10:
        try:
            data = urllib.urlopen(page_url).read()
            break
        except:
            try_count += 1
    else:
        message = 'Can not access to the proxy web.'
        logutil.log(message)
        print message
        return []
    proxyList = re.findall(r"(?<=<TR align=\"center\" bgcolor=\"#fbfbfb\" onDblClick=\"clip\(\')(\d+.\d+.\d+.\d+:\d+)", data)
    return testProxyViaMultiThread(proxyList), len(proxyList) < proxy_number_per_page

def getCheckedProxyListFromCnProxy(page_access_number):
    page_url = urlCnProxySrc % page_access_number
    print 'Begin to check the proxy list from web %s.' % page_url
    try_count = 0
    while try_count < 10:
        try:
            data = urllib.urlopen(page_url).read()
            break
        except:
            try_count += 1
    else:
        message = 'Can not access to the cn proxy web.'
        logutil.log(message)
        print message
        return []
    proxyList = re.findall(r'(?<=<tr><td>)\d+\.\d+\.\d+\.\d+.*?(?=</td>)', data)
    proxy_list = []
    for each_proxy in proxyList:
        '''
        z="3";m="4";k="2";l="9";d="0";b="5";i="7";w="6";r="8";c="1"
        '''
        each_proxy = re.sub(r'\+z', '3', each_proxy)
        each_proxy = re.sub(r'\+m', '4', each_proxy)
        each_proxy = re.sub(r'\+k', '2', each_proxy)
        each_proxy = re.sub(r'\+l', '9', each_proxy)
        each_proxy = re.sub(r'\+d', '0', each_proxy)
        each_proxy = re.sub(r'\+b', '5', each_proxy)
        each_proxy = re.sub(r'\+i', '7', each_proxy)
        each_proxy = re.sub(r'\+w', '6', each_proxy)
        each_proxy = re.sub(r'\+r', '8', each_proxy)
        each_proxy = re.sub(r'\+c', '1', each_proxy)
        each_proxy = re.sub(r'[^\d.:]', '', each_proxy)
        each_proxy = re.sub(r'\.:', ':', each_proxy)
        proxy_list.append(each_proxy)
    return testProxyViaMultiThread(proxy_list), len(proxy_list) < proxy_number_per_page

def testProxyViaMultiThread(proxy_list_for_testing):
    proxy_tested_list = []
    proxy_queue = Queue.Queue()
    for each_proxy in proxy_list_for_testing:
        proxy_queue.put(each_proxy)
    mutex = threading.Lock()
    test_proxy_thread_list = []
    for i in range(10): #@UnusedVariable
        test_proxy_thread = TestProxy.TestProxy(proxy_queue, proxy_tested_list, mutex, test_url, key_word)
        test_proxy_thread_list.append(test_proxy_thread)
        test_proxy_thread.start()
    for each_test_proxy_thread in test_proxy_thread_list:
        each_test_proxy_thread.join()
    print 'The proxy list is follow:'
    for each_proxy in proxy_tested_list:
        print each_proxy
    return proxy_tested_list

def getCheckedProxy(count, page_access_max_number):
    proxy_list = getCheckedProxyListFromFile()
    page_access_number = 0;
    while len(proxy_list) < count and (page_access_number < page_access_max_number or page_access_max_number == 0):
        print str(page_access_number), str(page_access_max_number) 
        print 'The number of proxies is %d and less than %d.' % (len(proxy_list), count)
        page_access_number += 1
#        proxy_list_from_web, end_sign = getCheckedProxyListFromWeb(page_access_number)
        proxy_list_from_web, end_sign = getCheckedProxyListFromCnProxy(page_access_number)
        proxy_list.extend(proxy_list_from_web)
        if end_sign:
            print 'The last proxy web accessed is the end page.'
            break
    print 'The final number of proxies is %d.' % len(proxy_list)
    return proxy_list

def writeProxyFile(count = default_proxy_count, page_access_max_number = 1):
    print 'Begin to write proxy file.'
    proxy_list_file_content = '\n'.join(getCheckedProxy(count, page_access_max_number))
    rawProxyList = open(rawProxyListFileName, "w")
    rawProxyList.write(proxy_list_file_content)
    rawProxyList.close()

if __name__ == '__main__':
    writeProxyFile(page_access_max_number = 0)
