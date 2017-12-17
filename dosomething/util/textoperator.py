 # -*- coding: utf-8 -*-

'''
Created on 2010-8-28

@author: sixi
'''

import re
import webutil

def untag(text):
    text = text.strip()
    text = unWholeTag(text)
    text = re.sub(r'</?p>', '\n', text)
    text = re.sub(r'((<br>|<BR>|<br/>|<BR/>|<br />|<BR />)\s*)+', '\n', text)
    text = re.sub(r'</?[^>]+>', '', text)
    text = re.sub(r'(\n[ \t\r\f\v]*){2,}', '\n\n', text)
    text = replaceCharEntity(text)
    text = text.strip()
    return text
def untagWQ(text):
     text = text.strip()
     text = unWholeTag(text)
     text = re.sub(r'</?p>', '\n', text)
     text = re.sub(r'((<br>|<BR>|<br/>|<BR/>|<br />|<BR />)\s*)+', '\n', text)
     text = re.sub(r'</?[^>]+">', '', text)
     text = re.sub(r'(\n[ \t\r\f\v]*){2,}', '\n\n', text)
     text = re.sub("\'",'',text)
     text = re.sub('\\\\','',text)
     text = re.sub("'",'\\\'',text)
     text = replaceCharEntity(text)
     text = text.strip()
     return text
def deleHtml(text):
    text = text.strip()
    text = re.sub('.html','',text)

def untagR(text):
    return re.sub(r'\r', '', untag(text)).strip()

def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ', '160':' ',
                   'lt':'<', '60':'<',
                   'gt':'>', '62':'>',
                   'amp':'&', '38':'&',
                   'quot':'"', '34':'"',}
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()
        key=sz.group('name')
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def unWholeTag(text):
    tag_name = ['script']
    for each_tag_name in tag_name:
        text = unOneWholeTag(text, each_tag_name)
    return text

def unOneWholeTag(text, tag_name):
    untag_compile = re.compile(r'<%s.*?</%s>' % (tag_name, tag_name), re.I | re.S)
    return untag_compile.sub('', text)

def findThing(regex, content, flags=0):
    search_result = re.search(regex, content, flags)
    if search_result:
        return search_result.group()
    else:
        return ''

def str2int(str):
    try:
        return int(str)
    except:
        return 0

def str2float(str):
    try:
        return float(str)
    except:
        return 0.0

if __name__=='__main__':
    url = 'http://live.damai.cn/bj/Ticket_19093.html'
    content = webutil.get(url)
    print untag(content)
