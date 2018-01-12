#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.model.BaseInfoEntity import BaseInfoEntity
from lianjia.model.DealInfoEntity import DealInfoEntity
from lianjia.model.HouseTypeDetailsEntity import HouseTypeDetailsEntity
from lianjia.model.LocationDetailsEntity import LocationDetailsEntity
from lianjia.model.ViewHouseHistoryListEntity import ViewHouseHistoryListEntity
from lianjia.model.EstateDetailEntity import EstateDetailEntity

class DetailEntity(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        '''房源编号'''
        self.lianjiaHouseIndex = ''
        '''详情标题'''
        self.title = ''
        '''房屋价格'''
        self.priceNum = 0
        self.baseInfoEntity = BaseInfoEntity()
        self.dealInfoEntity = DealInfoEntity()
        self.locationDetailsEntity = LocationDetailsEntity()
        self.houseTypeDetailsEntityList = []
        self.estateDetailEntity = EstateDetailEntity()
        self.viewHouseHistoryListEntity = ViewHouseHistoryListEntity()
        pass
