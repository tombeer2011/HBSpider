#encoding: utf-8
'''
Created on Jan 5, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.downloder.Downloader import Downloader
from lianjia.parser.Parser import Parser
from lianjia.storage.Storage import Storage
from lianjia.config.Config import Config

class Manager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.downloader = Downloader()

    def test(self):
        dl = Downloader()
        dl.test()
    
        pa = Parser()
        pa.test()
    
        st = Storage()
        st.test()
        self.getDetailLinks(1)
    '''
    获取所有列表信息里的详情URL
    '''
    def getAllDetailLinks(self,pageCount):
        urlList = []
        for i in range(pageCount):
            urlList.append(self.getDetailLinks(i))
        # print(urlList)
        print('urlList len ' + str(len(urlList)))
        return urlList
        pass

    '''
    获取列表信息里的详情URL
    '''
    def getDetailLinks(self,index):
        html = self.downloader.downloadHtmlContent(Config.LIANJIA_ERSHOUFANG_LIST + str(index))
        return self.downloader.getUrlList(html)
        pass

    def getDetailHtml(self):
        html = self.downloader.downloadHtmlContent()

        pass