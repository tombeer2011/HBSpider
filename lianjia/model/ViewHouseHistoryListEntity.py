#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class ViewHouseHistoryListEntity(object):
    '''
    classdocs
    '''


    '''累计看房次数'''
    totalTimes = 0
    '''最近7天看房客户数'''
    viewHouseUsers = 0
    '''看房详细记录'''
    ViewHouseHistoryEntityList = []

    def __init__(self):
        '''
        Constructor
        '''