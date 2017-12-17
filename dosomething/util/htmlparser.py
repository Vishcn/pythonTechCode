# -*- coding: utf-8 -*-
'''
Created on Sep 26, 2010

@author: sixi
'''

import re

NO_ATTR = 'no_attr'

def getTextByTagName(tag_name, content, attribute_string=''):
    if attribute_string == '':
        text_search = re.compile(r'(?:<%s[^>]*?>)(.*?)(?=</%s>)' % (tag_name, tag_name), re.S).search(content)
        if text_search:
            return text_search.group(1)
    elif NO_ATTR == attribute_string:
        text_search = re.compile(r'(?<=<%s>).*?(?=</%s>)' % (tag_name, tag_name), re.S).search(content)
        if text_search:
            return text_search.group()
    else:
        text_search = re.compile(r'(?<=<%s %s>).*?(?=</%s>)' % (tag_name, attribute_string, tag_name), re.S).search(content)
        if text_search:
            return text_search.group()
    return ''
def getAllTagsByTagEn(star_tag, end_tag, content):
    return re.compile(r'<%s>.*?</%s>' % (star_tag, end_tag), re.S).findall(content)
def getAllTextsByTagName(tag_name, content, attribute_string=''):
    if attribute_string == '':
        return re.compile(r'(?:<%s[^>]*?>)(.*?)(?=</%s>)' % (tag_name, tag_name), re.S).findall(content)
    elif NO_ATTR == attribute_string:
        return re.compile(r'(?<=<%s>).*?(?=</%s>)' % (tag_name, tag_name), re.S).findall(content)
    else:
        return re.compile(r'(?<=<%s %s>).*?(?=</%s>)' % (tag_name, attribute_string, tag_name), re.S).findall(content)

def getTagByTagName(tag_name, content, attribute_string=''):
    if attribute_string == '':
        text_search = re.compile(r'<%s[^>]*?>.*?</%s>' % (tag_name, tag_name), re.S).search(content)
        if text_search:
            return text_search.group()
    elif NO_ATTR == attribute_string:
        text_search = re.compile(r'<%s>.*?</%s>' % (tag_name, tag_name), re.S).search(content)
        if text_search:
            return text_search.group()
    else:
        text_search = re.compile(r'<%s %s>.*?</%s>' % (tag_name, attribute_string, tag_name), re.S).search(content)
        if text_search:
            return text_search.group()
    return ''

def getAllTagsByTagName(tag_name, content, attribute_string=''):
    if attribute_string == '':
        return re.compile(r'<%s[^>]*?>.*?</%s>' % (tag_name, tag_name), re.S).findall(content)
    elif NO_ATTR == attribute_string:
        return re.compile(r'<%s>.*?</%s>' % (tag_name, tag_name), re.S).findall(content)
    else:
        return re.compile(r'<%s %s>.*?</%s>' % (tag_name, attribute_string, tag_name), re.S).findall(content)
def getAllTagsByTagNameAll(tag_name, content, attribute_string=''):
    if attribute_string == '':
        return re.compile(r'<%s[^>]*?>.*?</%s>' % (tag_name, tag_name), re.S).findall(content)
    elif NO_ATTR == attribute_string:
        return re.compile(r'<%s>.*?</%s>' % (tag_name, tag_name), re.S).findall(content)
    else:
        return re.compile(r'<%s [^>]*?%s[^>]*?>.*?</%s>' % (tag_name, attribute_string, tag_name), re.S).findall(content)

def hasTag(tag_name, content, attribute_string=''):
    if attribute_string == '':
        text_search = re.compile(r'<%s[^>]*?>.*?</%s>' % (tag_name, tag_name), re.S).search(content)
        if text_search:
            return True
    else:
        text_search = re.compile(r'<%s %s>.*?</%s>' % (tag_name, attribute_string, tag_name), re.S).search(content)
        if text_search:
            return True
    return False

def delTagByTagName(tag_name, content, attribute_string=''):
    if attribute_string == '':
        return re.compile(r'<%s[^>]*?>.*?</%s>' % (tag_name, tag_name), re.S).sub('', content)
    else:
        return re.compile(r'<%s %s>.*?</%s>' % (tag_name, attribute_string, tag_name), re.S).sub('', content)

def delTagSymbolByTagName(tag_name, content, count=0):
    return re.compile(r'</?%s[^>]*?>' % tag_name, re.S).sub('', content, count)
#add by keven
def getinTextbyTag(tag_name,content,ltag):
    res=''
    text_search = re.compile(r'(?:<%s[^>])(.*?)(?=\>)' % tag_name, re.S).search(content) 
    if text_search:
        attribute_string = content[text_search.start():text_search.end()]
        attribute_spilt=re.search(r'(?<=%s=\").*?(?=\")' % ltag, attribute_string)
        if attribute_spilt:
            res = attribute_string[attribute_spilt.start():attribute_spilt.end()]
    return res
def delCDATATag(rawString):
    CDATA_content_search = re.compile(r'(?<=<!\[CDATA\[).*?(?=\]\]>)', re.S).search(rawString)
    if CDATA_content_search:
        return CDATA_content_search.group()
    else:
        return rawString

if __name__ == '__main__':
    print getTextByTagName('a', '<a href=\'xxx\'>this is....</a>')
    print getTextByTagName('a', '<a href=\'xxx\'>this is....</a>', 'href=\'xxx\'')
    print getTextByTagName('a', '<a>this is....</a>', NO_ATTR)
    print getAllTextsByTagName('a', '<a href=\'xxx\'>this is....</a><a href=\'xxx\'>this is....</a>')
    print getAllTextsByTagName('a', '<a href=\'xxx\'>this is....</a><a href=\'xxx\'>this is....</a>', 'href=\'xxx\'')
    print getTagByTagName('a', '<a href=\'xxx\'>this is....</a>')
    print getTagByTagName('a', '<a href=\'xxx\'>this is....</a>', 'href=\'xxx\'')
    print getAllTagsByTagName('a', '<a href=\'xxx\'>this is....</a><a href=\'xxx\'>this is....</a>')
    print getAllTagsByTagName('a', '<a href=\'xxx\'>this is....</a><a href=\'xxx\'>this is....</a>', 'href=\'xxx\'')
    print getAllTagsByTagNameAll('a', '<a sshref=\'xxx\'>this is....</a><a href=\'xxx\' aa>this is....</a>', 'href=\'xxx\'')
    print delTagByTagName('a', '<a href=\'xxx\'>this is....</a>that is ....')
    print delTagSymbolByTagName('a', '<a href=\'xxx\'>this is....</a>')
    print delTagSymbolByTagName('a', '<a href=\'xxx\'>this is....</a>', 1)