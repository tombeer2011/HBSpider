#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class DealInfoEntity(object):
    '''
    classdocs
    '''



    def __init__(self):
        '''
        Constructor
        '''
        '''上次交易时间'''
        self.lastDealTime = ''
        '''房本年限'''
        self.housePeriod = ''
        '''售房原因'''
        self.sellReason = ''
        '''房屋类型'''
        self.houseClass = ''