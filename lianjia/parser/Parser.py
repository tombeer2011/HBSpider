#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from bs4 import BeautifulSoup
import json

from lianjia.config.Config import Config
from lianjia.comm.ReUtils import ReUtils
from lianjia.model.DetailEntity import DetailEntity
from lianjia.model.BaseInfoEntity import BaseInfoEntity
from lianjia.model.DealInfoEntity import DealInfoEntity
from lianjia.model.HouseTypeDetailsEntity import HouseTypeDetailsEntity
from lianjia.model.LocationDetailsEntity import LocationDetailsEntity
import types
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
        tmp  = element.find_all('a',attrs = {'class':'text link-hover-green js_triggerGray js_fanglist_title'})
        for i in range(len(tmp)):
            urlList.append(Config.LIANJIA_DOMAIN + str(tmp[i].attrs['href']))
        # print (urlList)
        return urlList



    '''
    获取每个房源的详细信息
    '''
    def passerContentDetail(self,html):

        element = BeautifulSoup(html,'html.parser')

        detailEntity = DetailEntity()
        tmp = element.find_all('ul',attrs = {'class':'baseinfo-tb'})
        '''获取房屋信息标题'''
        detailEntity.title = element.find('h1',attrs = {'class':'header-title'}).string.strip()
        detailEntity.lianjiaHouseIndex = element.find()
        tmp = element.find_all('span',attrs = {'class':'price-num'})
        detailEntity.priceNum = tmp[0].text.strip()

        detailEntity.baseInfoEntity = self.passerBaseInfo(element)
        detailEntity.dealInfoEntity = self.passerDealInfo(element)
        detailEntity.locationDetailsEntity = self.passerLocationDetails(element)
        detailEntity.lianjiaHouseIndex = detailEntity.locationDetailsEntity.lianjiaHouseIndex
        return detailEntity
        pass

    '''解析房源基本信息'''
    def passerBaseInfo(self,element):
        baseInfoEntity = BaseInfoEntity()
        tmp = element.find_all('div',attrs = {'class':'module-col baseinfo-col2'})
        str = tmp[0].text
        list = str.split('\n')
        for i in range(len(list)):
            if(list[i] == u'房屋户型'):
                baseInfoEntity.houseTypeRoomNum = list[i + 1].strip()
            if(list[i] == u'配备电梯'):
                baseInfoEntity.lift = list[i + 1].strip()
            if(list[i] == u'建筑面积'):
                baseInfoEntity.houseArea = list[i + 1].strip()
            if(list[i] == u'供暖方式'):
                baseInfoEntity.heatingMethod = list[i + 1].strip()

        tmp = element.find_all('div',attrs = {'class':'module-col baseinfo-col3'})
        str = tmp[0].text
        list = str.split('\n')
        for i in range(len(list)):
            if(list[i] == u'所在楼层'):
                baseInfoEntity.houseFloor = list[i + 1].strip()
            if(list[i] == u'装修情况'):
                baseInfoEntity.houseDecorate = list[i + 1].strip()
            if(list[i] == u'房屋朝向'):
                baseInfoEntity.houseOrientation = list[i + 1].strip()
            if(list[i] == u'车位情况'):
                baseInfoEntity.isParkingLot = list[i + 1].strip()

        tmp = element.find_all('p',attrs = {'class':'u-mt8 u-fz12'})
        baseInfoEntity.houseCreateTime = tmp[2].text.replace('\n','').strip()
        return baseInfoEntity

    ''''解析交易信息'''
    def passerDealInfo(self,element):
        dealInfo = DealInfoEntity()
        tmp = element.find_all('div', attrs = {'class': 'module-col baseinfo-col2'})
        str = tmp[1].text
        str = ReUtils.trimFLEnter(str)
        list = ReUtils.replacEnter(str)
        # list = str.split('\n')
        for i in range(len(list)):
            if(list[i] == u'上次交易'):
                dealInfo.lastDealTime = list[i + 1].strip()
            if(list[i] == u'房本年限'):
                dealInfo.housePeriod = list[i + 1].strip()

        tmp = element.find_all('div', attrs = {'class': 'module-col baseinfo-col3'})
        str = tmp[1].text
        str = ReUtils.trimFLEnter(str)
        list = ReUtils.replacEnter(str)
        # list = str.split('\n')
        for i in range(len(list)):
            if(list[i] == u'售房原因'):
                dealInfo.sellReason = list[i + 1].strip()
            if(list[i] == u'房屋类型'):
                dealInfo.houseClass = list[i + 1].strip()
        return dealInfo
        pass

    '''解析房屋位置信息'''
    def passerLocationDetails(self,element):
        locationDetails = LocationDetailsEntity()
        tmp = element.find_all('ul',attrs = {'class':'maininfo-minor maininfo-item'})
        str = tmp[0].text
        str = ReUtils.trimFLEnter(str)
        list = ReUtils.replacEnter(str)
        for i in range(len(list)):
            if(list[i] == u'环线信息'):
                locationDetails.cycleInfo = list[i + 1].strip()
            if(list[i] == u'所在地址'):
                locationDetails.estateAddress = list[i +1].strip()
            if(list[i] == u'房源编号'):
                locationDetails.lianjiaHouseIndex = list[i + 1].strip()

        tmp = element.find_all('span',attrs = {'class':'maininfo-estate-name'})
        list = tmp[0].contents
        for i in range(len(list)):
            if(i == 0):
                locationDetails.estateName = list[i].text.strip()
            if(i == 2):
                locationDetails.districtName = list[i].text.strip()
            if(i == 4):
                locationDetails.businessDistrictName = list[i].text.strip()
        tmp = element.find_all('span',attrs = {'class':'item-cell maininfo-estate-address'})
        locationDetails.estateAddress = tmp[0].text
        return locationDetails
        pass

    '''解析房屋信息的json数据'''
    def passerHouseRoomsDetails(self,jsonText):
        jsonDict = dict()
        jsonData = json.loads(jsonText)
        result = []
        if(jsonData['cellInfoList'] != None):
            list = jsonData['cellInfoList']
            for i in range(len(list)):
                houseTypeDetails = HouseTypeDetailsEntity()
                tmpKeys = dict(list[i])
                if(tmpKeys.has_key('area')):
                    houseTypeDetails.roomArea = list[i]['area']
                if (tmpKeys.has_key('face')):
                    houseTypeDetails.roomOrientation = list[i]['face']
                if (tmpKeys.has_key('name')):
                    houseTypeDetails.roomName = list[i]['name']
                if (tmpKeys.has_key('windowTypeName')):
                    houseTypeDetails.roomWindowType = list[i]['windowTypeName']
                result.append(houseTypeDetails)
        return result
        pass

