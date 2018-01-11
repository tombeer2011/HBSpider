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

    ''''带看经纪人'''
    userName = ''
    '''带看时间'''
    time = ''
    '''带看人次数'''
    userNameTimes = 0

    def __init__(self):
        '''
        Constructor
        '''
