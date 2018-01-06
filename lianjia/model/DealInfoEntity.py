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

    '''上次交易时间'''
    lastDealTime = ''
    '''房本年限'''
    housePeriod = ''
    '''售房原因'''
    sellReason = ''
    '''房屋类型'''
    houseClass = ''

    def __init__(self):
        '''
        Constructor
        '''