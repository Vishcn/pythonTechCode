# -*- coding: utf-8 -*-

import logutil
import re
import urllib
import urllib2

def post(url, key, con):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    search = urllib.urlencode([(key, con)])
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req, search).read()
    return fd

def get(url):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    try:
        logutil.logger.logger.info('Try to get the content of %s.' % url)
        content = urllib2.urlopen(req).read()
    except:
        content = ''
    return content

def getPageFromUrl(url):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    try:
        content = urllib2.urlopen(req).read()
    except:
        content = ''
    return content

def validateURL(url):
    if re.match(r'http://', url):
        return True
    else:
        return False

if __name__ == '__main__':
    print validateURL('http://kkkkkkkk')
