#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from bs4 import BeautifulSoup

from lianjia.config.Config import Config
class Parser(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def test(self):
        print('parser test')
        
    '''
    获取Url链接列表
    '''
    def parserUrlList(self,html):
        urlList = []

        element = BeautifulSoup(html,'html.parser')
        tmp  = element.find_all('a',attrs={'class':'text link-hover-green js_triggerGray js_fanglist_title'})
        for i in range(len(tmp)):
            urlList.append(Config.LIANJIA_DOMAIN + str(tmp[i].attrs['href']))
        # print (urlList)
        return urlList
    
    '''
    获取每个房源的详细信息
    '''
    def passerContentDetail(self,html):

        pass
        