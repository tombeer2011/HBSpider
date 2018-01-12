#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class HouseTypeDetailsEntity(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        '''房间名称'''
        self.roomName = ''
        '''房间面积'''
        self.roomArea = 0.0
        '''房间朝向'''
        self.roomOrientation = ''
        '''房间窗户类型'''
        self.roomWindowType = ''