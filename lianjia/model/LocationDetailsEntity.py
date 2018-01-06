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

    '''环线信息'''
    cycleInfo = ''
    '''小区名称'''
    estateName = ''
    '''城区名称'''
    districtName = ''
    '''商圈板块名称'''
    businessDistrictName = ''
    '''小区所在地址'''
    estateAddress = ''
    '''房源编号'''
    lianjiaHouseIndex = ''

    def __init__(self):
        '''
        Constructor
        '''