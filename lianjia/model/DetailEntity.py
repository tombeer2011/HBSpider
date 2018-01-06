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
from lianjia.model.ViewHouseHistoryEntity import ViewHouseHistoryEntity

class DetailEntity(object):
    '''
    classdocs
    '''

    '''房源编号'''
    lianjiaHouseIndex = ''
    '''详情标题'''
    title=''
    '''房屋价格'''
    priceNum = 0

    def __init__(self):
        '''
        Constructor
        '''
        self.baseInfoEntity = BaseInfoEntity()
        self.dealInfoEntity = DealInfoEntity()
        self.houseTypeDetailsEntity = HouseTypeDetailsEntity()
        self.locationDetailsEntity = LocationDetailsEntity()
        pass
