#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class LocationDetailsEntity(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        '''环线信息'''
        self.cycleInfo = ''
        '''小区名称'''
        self.estateName = ''
        '''城区名称'''
        self.districtName = ''
        '''商圈板块名称'''
        self.businessDistrictName = ''
        '''小区所在地址'''
        self.estateAddress = ''
        '''房源编号'''
        self.lianjiaHouseIndex = ''