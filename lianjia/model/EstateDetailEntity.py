#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class EstateDetailEntity(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        '''	挂牌均价'''
        self.averagePrice = 0

        '''楼栋总数'''
        self.buildingTotalNum = 0
        '''房屋总数'''
        self.houseTotalNum = 0
        '''物业公司'''
        self.propertyManagementCompany = ''
        '''开发商'''
        self.developers = ''
        '''挂牌房源正在销售'''
        self.sellingHouseNum = 0
        '''挂牌房源正在出租'''
        self.rentHouseNum = 0