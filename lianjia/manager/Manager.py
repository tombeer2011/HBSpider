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
from lianjia.comm.ReUtils import ReUtils

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
        self.dl = Downloader()
        self.dl.test()

        self.pa = Parser()
        self.pa.test()

        self.st = Storage()
        self.st.test()
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

    '''
    获取每个房源的详细信息
    '''
    def getDetailHtml(self,url):
        html = self.downloader.downloadHtmlContent(url)
        detailEntity = self.downloader.getDetailObj(html)

        '''获取每个房屋的每个房间的详细信息'''
        houseIndex = ReUtils.getNumeric(detailEntity.lianjiaHouseIndex)
        detailEntity.houseTypeDetailsEntityList = self.getHouseRoomsDetails(Config.LIANJIA_ROOMS_DATAIL.format(houseIndex[0]))

        return detailEntity
        pass

    '''获取房屋每个房间的详细信息'''
    def getHouseRoomsDetails(self,url):
        jsonText = self.downloader.getJson(url)
        return self.downloader.getHouseRoomsDetail(jsonText.encode('utf-8'))
        pass

    '''获取看房记信息'''
    def getViewHouseHistoryList(self,url):
        html = self.downloader.downloadHtmlContent(url)
        viewHouseHistoryListEntity = self.downloader.getViewHouseHistoryListEntity(html)
        return viewHouseHistoryListEntity
        pass