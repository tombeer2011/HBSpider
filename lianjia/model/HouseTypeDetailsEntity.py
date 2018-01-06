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

    '''房间名称'''
    roomName = ''
    '''房间面积'''
    roomArea = 0.0
    '''房间朝向'''
    roomOrientation = ''
    '''房间窗户类型'''
    roomWindowType = ''
    def __init__(self):
        '''
        Constructor
        '''