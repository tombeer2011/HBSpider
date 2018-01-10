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

    '''	挂牌均价'''
    averagePrice = 0

    '''楼栋总数'''
    buildingTotalNum = 0
    '''房屋总数'''
    houseTotalNum = 0
    '''物业公司'''
    propertyManagementCompany = ''
    '''开发商'''
    developers = ''
    '''挂牌房源正在销售'''
    sellingHouseNum = 0
    '''挂牌房源正在出租'''
    rentHouseNum = 0

    def __init__(self):
        '''
        Constructor
        '''