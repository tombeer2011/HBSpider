#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

import requests
import urllib2

from lianjia.parser.Parser import Parser

class Downloader(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
        }

    '''
    classdocs
    '''  
    def __init__(self):
        self.parser = Parser()
        '''
        Constructor
        '''
         
    def test(self):
        print('Downloader test')
        print('test hash')
        
    '''
    根据主要url下载html信息
    '''
    def downloadHtmlContent(self, mainUrl):
        print ('downloadUrls start  \n'+mainUrl)
        # 获取主页面信息
        request = requests.get(url=mainUrl)
        html = request.content
        return html
        pass

    '''
    获取url列表
    '''
    def getUrlList(self,html):
        return self.parser.parserUrlList(html)

    '''
    根据html内容解析详细信息
    '''
    def getDetailObj(self,html):
        return self.parser.passerContentDetail(html)
        pass

    '''获取Json数据'''
    def getJson(self,url):
        request = requests.get(url)
        jsonText = request.content
        return jsonText
        pass

    '''获取房屋每个房间的详细信息'''
    def getHouseRoomsDetail(self,jsonText):
        return self.parser.passerHouseRoomsDetails(jsonText)
        pass

    '''获取看房记录信息实体'''
    def getViewHouseHistoryListEntity(self,html):
        return self.parser.passerViewHouseHistory(html)
        pass