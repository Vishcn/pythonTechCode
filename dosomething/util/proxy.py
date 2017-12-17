#!/usr/share/python
# -*- coding: utf-8 -*-
# Filename: proxy.py

import logutil
import random
import re
import socket
import traceback
import urllib
import urllib2

max_try_number = 10

headers_list = [
{'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6', 'X-Forwarded-For':'http://127.0.0.1'}
]

class Proxy:

    def __init__(self, proxy_list='proxy_list', defaulttimeout=30):
        proxy_file = file(proxy_list, "r")
        self.proxy = (proxy_file.read())[:-1].split('\n')
        self.index = random.randint(0, len(self.proxy) - 1)
        self.defaulttimeout = defaulttimeout
        socket.setdefaulttimeout(self.defaulttimeout)
        print 'initializd the proxy class via file', proxy_list, 'and set default timeout', str(self.defaulttimeout)

    def nextproxy(self):
        self.index = (self.index + 1) % len(self.proxy)
        print 'return', self.proxy[self.index], 'as proxy'

    def getrandproxy(self):
        proxy_address = random.choice(self.proxy)
        logutil.logger.logger.debug('return %s as proxy at random.' % proxy_address)
        return proxy_address

    def getproxy(self):
        proxy_address = self.proxy[self.index]
        return proxy_address

    def getproxyIPandPort(self):
        IP_Port = self.proxy[self.index].split(':')
        return IP_Port[0], IP_Port[1]

    def getcontent(self, url, validate_word=r'大麦', charset='utf-8', count=1, max_count=0, fatal_count=1, max_fatal_count=3):
        if (0 == max_count and count > len(self.proxy)) or (0 != max_count and count > max_count):
            raise Exception('Can not get the webpage content with max_count = %d.' % max_count)
        if 0 != max_fatal_count and fatal_count > max_fatal_count:
            raise Exception('Can not get the webpage content with max_fatal_count = %d.' % max_fatal_count)
        proxy_address = self.getproxy()
        proxy_support = urllib2.ProxyHandler({'http':'http://' + proxy_address})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        headers = {
          'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6',
          #'Referer':'http://damai.cn/',
          'X-Forwarded-For':'http://127.0.0.1'
        }
        req = urllib2.Request(
            url=url,
            headers=headers
        )
        print 'using', proxy_address, 'to request', url
        try:
            response = urllib2.urlopen(req)

            content = response.read()
            if '' == validate_word:
                return content
            if charset != 'utf-8':
                content = content.decode(charset, 'ignore').encode('utf-8', 'ignore')
            damaiSign = re.search(validate_word, content)
            if damaiSign:
                print 'proxy: the page is aim, so go ahead.'
                return content
            else:
                print 'proxy: the page is not aim, so continue.'
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count,
                  max_fatal_count=max_fatal_count
                )
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'proxy: URLError has attr reason, so continue.'
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count,
                  max_fatal_count=max_fatal_count
                )
            else:
                print 'proxy: URLError has not attr reason.'
                #raise e
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count + 1,
                  max_fatal_count=max_fatal_count
                )
        except:
            print 'proxy: Unexcepted Exception.'
            traceback.print_exc()
            self.nextproxy()
            return self.getcontent(
              url=url,
              validate_word=validate_word,
              charset=charset,
              count=count + 1,
              max_count=max_count,
              fatal_count=fatal_count,
              max_fatal_count=max_fatal_count
            )
    
    def getHuWaicontent(self, url, validate_word=r'户外', charset='utf-8', count=1, max_count=0, fatal_count=1, max_fatal_count=3):
        if (0 == max_count and count > len(self.proxy)) or (0 != max_count and count > max_count):
            raise Exception('Can not get the webpage content with max_count = %d.' % max_count)
        if 0 != max_fatal_count and fatal_count > max_fatal_count:
            raise Exception('Can not get the webpage content with max_fatal_count = %d.' % max_fatal_count)
        proxy_address = self.getproxy()
        proxy_support = urllib2.ProxyHandler({'http':'http://' + proxy_address})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        header = []
        x_forward_address = proxy_address.split(':')[0]
        header.append({'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:9.0.1) Gecko/20100101 Firefox/9.0.1',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
        header.append({'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
                       'X-Forwarded-For':'http://' + x_forward_address,
                       'Referer':'http://bbs.8264.com/'})
    
        header_number = random.randint(0,7)
    
        headers = header[header_number]
        
        req = urllib2.Request(
            url=url,
            headers=headers
        )
#        headers = {
#          'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6',
#          #'Referer':'http://damai.cn/',
#          'X-Forwarded-For':'http://127.0.0.1'
#        }
#        req = urllib2.Request(
#            url=url,
#            headers=headers
#        )
        print 'using', proxy_address, 'to request', url
        try:
            response = urllib2.urlopen(req)

            content = response.read()
            print content
            if '' == validate_word:
                return content
            if charset != 'utf-8':
                content = content.decode(charset, 'ignore').encode('utf-8', 'ignore')
                print content
            damaiSign = re.search(validate_word, content)
            if damaiSign:
                print 'proxy: the page is aim, so go ahead.'
                return content
            else:
                print 'proxy: the page is not aim, so continue.'
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count,
                  max_fatal_count=max_fatal_count
                )
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'proxy: URLError has attr reason, so continue.'
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count,
                  max_fatal_count=max_fatal_count
                )
            else:
                print 'proxy: URLError has not attr reason.'
                #raise e
                self.nextproxy()
                return self.getcontent(
                  url=url,
                  validate_word=validate_word,
                  charset=charset,
                  count=count + 1,
                  max_count=max_count,
                  fatal_count=fatal_count + 1,
                  max_fatal_count=max_fatal_count
                )
        except:
            print 'proxy: Unexcepted Exception.'
            traceback.print_exc()
            self.nextproxy()
            return self.getcontent(
              url=url,
              validate_word=validate_word,
              charset=charset,
              count=count + 1,
              max_count=max_count,
              fatal_count=fatal_count,
              max_fatal_count=max_fatal_count
            )
        

    def getcontentviapost(self, url, post_parameter, max_try_number=max_try_number, charset='utf-8', count=1):
        if (max_try_number != 0 and count > max_try_number) or count > len(self.proxy):
            raise Exception
        proxy_address = self.getproxy()
        proxy_support = urllib2.ProxyHandler({'http': 'http://%s' % proxy_address})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        headers = {'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6',
                   'X-Forwarded-For':'http://127.0.0.1'}
        req = urllib2.Request(url=url, headers=headers)
        encode_post_parameter = urllib.urlencode(post_parameter)
        print 'using', proxy_address, 'to request', url, 'via post'
        try:
            urlopen_object = urllib2.urlopen(req, encode_post_parameter)
            if urlopen_object.geturl() == url:
                if charset == 'gb2312':
                    content = urlopen_object.read().decode(charset, 'ignore').encode('utf-8', 'ignore')
                print 'proxy: the page is aim, so go ahead.'
                return content
            else:
                print 'proxy: the page is not aim, so continue.'
                self.nextproxy()
                return self.getcontentviapost(url, post_parameter, max_try_number, charset, count + 1)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'proxy: URLError has attr reason, so continue.'
                self.nextproxy()
                return self.getcontentviapost(url, post_parameter, max_try_number, charset, count + 1)
            else:
                print 'proxy: URLError has not attr reason.'
                self.nextproxy()
                return self.getcontentviapost(url, post_parameter, max_try_number, charset, count + 1)
        except:
            print 'proxy: Unexcepted Exception.'
            traceback.print_exc()
            self.nextproxy()
            return self.getcontentviapost(url, post_parameter, max_try_number, charset, count + 1)

    def getcontentwithoutproxy(self, url):
        headers = random.choice(headers_list)
#        headers = {
#          'User-Agent':'Mozillia/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100420 Firefox/3.5.6',
##         'Referer':'http://damai.cn/',
#          'X-Forwarded-For':'http://127.0.0.1'
#        }
        req = urllib2.Request(
            url=url,
            headers=headers
        )
        print 'using no proxy to request', url
        try:
            content = urllib2.urlopen(req).read()
#            print '------ proxy: the content is ------'
#            print content
#            print '-----------------------------------'
            return content
        except urllib2.URLError, e:
            raise e

    def getContentNew(self, url, charset='', output_charset='utf-8', max_count=3, with_proxy=True, allow_redirect=False):
        if '' == url:
            return None
        while max_count > 0:
            max_count -= 1
            try:
                if with_proxy:
                    proxy_address = self.getrandproxy()
                    proxy_support = urllib2.ProxyHandler({'http':'http://' + proxy_address})
                    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                    urllib2.install_opener(opener)
                    headers = random.choice(headers_list)
                    logutil.logger.logger.info('Using %s to request %s.' % (proxy_address, url))
                    req = urllib2.Request(url=url, headers=headers)
                else:
                    opener = urllib2.build_opener(urllib2.HTTPHandler)
                    urllib2.install_opener(opener)
                    logutil.logger.logger.info('Using no proxy to request %s.' % url)
                    req = urllib2.Request(url)
                response = urllib2.urlopen(req)
                response_url = response.geturl()
                logutil.logger.logger.debug('The original URL is %s, and the URL fetched is %s.' % (url, response_url))
                if not allow_redirect and url != response_url:
                    continue
                content = response.read()
                if '' == charset:
                    info = response.info()
                    if info.has_key('Content-Type'):
                        charset_search = re.search(r'charset=([\w-]*)', info['Content-Type'])
                        if charset_search:
                            charset = charset_search.group(1)
                if '' == charset:
                    charset_search = re.search(r'charset=([-\w"]*)', content)
                    if charset_search:
                        charset = re.sub('"', '', charset_search.group(1))
                if charset != '' and charset != output_charset:
                    content = content.decode(charset, 'ignore').encode(output_charset, 'ignore')
                return content
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    logutil.logger.logger.debug('We failed to reach a server. Reason: %s.' % e.reason)
                elif hasattr(e, 'code'):
                    logutil.logger.logger.debug('The server couldn\'t fulfill the request. Error code: %d.' % e.code)
            else:
                pass

if __name__ == '__main__':
    proxy_class = Proxy()
#    print proxy_class.getContentNew(url='http://www.dianping.com/citylist')
#    print proxy_class.getContentNew('http://www.baidu.com')
    print proxy_class.getContentNew('http://www.228.com.cn/index.html')
