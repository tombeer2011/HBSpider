'''
Created on Jan 4, 2018

@author: hb
'''

class Downloader(object):
    mainUrl = ''
    rulList = []
    '''
    classdocs
    '''  
    def __init__(self):
        self.mainUrl = ''
        self.rulList = []
        '''
        Constructor
        '''
         
    def test(self):
        print('Downloader test')
        print('test hash')
        
    '''
    根据主要url下载url列表
    '''
    def downloadUrls(self,mainUrl):
        pass
    
    '''
    获取主要url
    '''
    def getMainUrl(self):
        return self.mainUrl
    
    '''
    获取url列表
    '''
    def getUrlList(self):
        return self.rulList
    