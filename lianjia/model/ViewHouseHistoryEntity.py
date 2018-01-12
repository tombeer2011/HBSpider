#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class ViewHouseHistoryEntity(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        ''''带看经纪人'''
        self.userName = ''
        '''带看时间'''
        self.time = ''
        '''带看人次数'''
        self.userNameTimes = 0