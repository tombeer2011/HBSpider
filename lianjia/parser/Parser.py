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
from lianjia.model.EstateDetailEntity import EstateDetailEntity
from lianjia.model.ViewHouseHistoryEntity import ViewHouseHistoryEntity
from lianjia.model.ViewHouseHistoryListEntity import ViewHouseHistoryListEntity
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
        detailEntity.priceNum = float(tmp[0].text.strip())

        detailEntity.baseInfoEntity = self.passerBaseInfo(element)
        detailEntity.dealInfoEntity = self.passerDealInfo(element)
        detailEntity.locationDetailsEntity = self.passerLocationDetails(element)
        detailEntity.lianjiaHouseIndex = detailEntity.locationDetailsEntity.lianjiaHouseIndex
        detailEntity.estateDetailEntity = self.passerEstateDetails(element)

        return detailEntity
        pass

    '''解析房源基本信息'''
    def passerBaseInfo(self,element):
        baseInfoEntity = BaseInfoEntity()
        tmp = element.find_all('div',attrs = {'class':'module-col baseinfo-col2'})
        str = tmp[0].text
        list = str.split('\n')
        for i in range(len(list)):
            if(list[i] != None):
                if(list[i] == u'房屋户型'):
                    roomsHalls = ReUtils.getRoomsHalls(list[i + 1].strip())
                    for j in range(len(roomsHalls)):
                        if(j == 0):
                            baseInfoEntity.houseTypeRoomNum = int(roomsHalls[j])
                        if(j == 1):
                            baseInfoEntity.houseTypeHallNum = int(roomsHalls[j])
                        if(j == 2):
                            baseInfoEntity.houseTypeBathNum = int(roomsHalls[j])
                if(list[i] == u'配备电梯'):
                    baseInfoEntity.lift = list[i + 1].strip()
                if(list[i] == u'建筑面积'):
                    baseInfoEntity.houseArea = float(ReUtils.getNumbericValue(list[i + 1].strip()))
                if(list[i] == u'供暖方式'):
                    baseInfoEntity.heatingMethod = list[i + 1].strip()

        tmp = element.find_all('div',attrs = {'class':'module-col baseinfo-col3'})
        str = tmp[0].text
        list = str.split('\n')
        for i in range(len(list)):
            if(list[i] != None):
                if(list[i] == u'所在楼层'):
                    # baseInfoEntity.houseFloor = list[i + 1].strip()
                    floors = ReUtils.getFloor(list[i + 1].strip())
                    for j in range(len(floors)):
                        if(j == 0):
                            baseInfoEntity.houseFloor = floors[j]
                        if(j == 1):
                            baseInfoEntity.houseTotalFloors = int(floors[j])
                if(list[i] == u'装修情况'):
                    baseInfoEntity.houseDecorate = list[i + 1].strip()
                if(list[i] == u'房屋朝向'):
                    baseInfoEntity.houseOrientation = list[i + 1].strip()
                if(list[i] == u'车位情况'):
                    baseInfoEntity.isParkingLot = list[i + 1].strip()

        tmp = element.find_all('p',attrs = {'class':'u-mt8 u-fz12'})
        baseInfoEntity.houseCreateTime = int(ReUtils.getNumbericValue(tmp[2].text.replace('\n','').strip()))
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
        if(jsonText == None or '' == jsonText):
            return []
        jsonDict = dict()
        jsonData = json.loads(jsonText)
        result = []
        if(jsonData['message'] == '暂无数据'):
            return result
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

    '''解析小区简介'''
    def passerEstateDetails(self,element):
        estateDetail = EstateDetailEntity()
        tmp = element.find_all('ul',attrs = {'class' : 'intro-detail'})
        if(tmp is not None and len(tmp) > 1):
            str = tmp[1].text
            str = ReUtils.trimFLEnter(str)
            list = ReUtils.replacEnter(str)
            for i in range(len(list)):
                if(list[i] == u'挂牌均价'):
                    estateDetail.averagePrice = float(ReUtils.getNumbericValue(list[i + 1]))
                if(list[i] == u'楼栋总数'):
                    estateDetail.buildingTotalNum = int(ReUtils.getNumbericValue(list[i + 1]))
                if(list[i] == u'房屋总数'):
                    estateDetail.houseTotalNum = int(ReUtils.getNumbericValue(list[i + 1]))
                if(list[i] == u'物业公司'):
                    estateDetail.propertyManagementCompany = list[i + 1]
                if(list[i] == u'开发商'):
                    estateDetail.developers = list[i + 1]
                if(list[i] == u'挂牌房源'):
                    estateDetail.sellingHouseNum = ReUtils.getNumbericValue(list[i +1])
                    if(i + 2 <= len(list)):
                        estateDetail.rentHouseNum = ReUtils.getNumbericValue(list[i + 2])
            pass
        return estateDetail
        pass

    '''获取JS代码'''
    def passerJS(self,element):
        tmp = element.get_text()
        pass

    '''获取看房记录实体'''
    def passerViewHouseHistory(self,html):
        element = BeautifulSoup(html, 'html.parser')
        viewHouseHistoryListEntity = ViewHouseHistoryListEntity()
        tmp = element.find_all('div', attrs={'class': 'list-ret'})
        if(len(tmp) > 0):
            numerList = tmp[0].find_all('span', attrs={'class', 'c-orange'})
            if(len(numerList) >=2 ):
                viewHouseHistoryListEntity.totalTimes = int(numerList[1].text)
                viewHouseHistoryListEntity.viewHouseUsers = int(numerList[0].text)

        tmp = element.find_all('ul', attrs = {'class','js_jiluList'})
        for i in range(len(tmp[0].find_all('span', attrs={'class', 'w-1'}))):
            # print(i)
            viewHouseHistoryEntity = ViewHouseHistoryEntity()
            viewHouseHistoryEntity.time = tmp[0].find_all('span', attrs={'class', 'w-1'})[i].text
            viewHouseHistoryEntity.userName = tmp[0].find_all('a', attrs={'class', 'w-2'})[i].text.split('(')[0]
            viewHouseHistoryEntity.userNameTimes = int(ReUtils.getNumeric(tmp[0].find_all('a', attrs={'class', 'w-2'})[i].text))
            viewHouseHistoryListEntity.viewHouseHistoryEntityList.append(viewHouseHistoryEntity)
        return viewHouseHistoryListEntity
        pass