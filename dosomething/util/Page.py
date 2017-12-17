'''
Created on Dec 15, 2010

@author: sixi
'''

class Page(object):
    '''
    classdocs
    '''

    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
        
        self.header = ''
        self.header_length = -1
        
        self.status_code = -1
        self.content_length = -1
        self.location = ''
        self.connection_state = False
        self.content_encoding = ''
        self.content_type = ''
        self.charset = ''
        self.transfer_encoding = ''
        
        self.content = ''
        self.len_content = -1
        self.no_tag_content = ''
        
        self.content_link_info = ''
    
    def Connection(self):
        pass
    
    def getContentLinkInfo(self):
        pass
