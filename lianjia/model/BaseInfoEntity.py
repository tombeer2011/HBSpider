#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class BaseInfoEntity(object):
    '''
    classdocs
    '''

    '''房屋户型'''
    houseTypeRoomNum = 0
    houseTypeHallNum = 0
    houseTypeBathNum = 0

    '''配备电梯'''
    lift = ''
    ''''''

    '''建筑面积'''
    houseArea = 0.0
    '''供暖方式'''
    heatingMethod = ''
    '''所在楼层'''
    houseFloor = ''
    '''总共层高'''
    houseTotalFloors = -1
    '''装修情况'''
    houseDecorate = ''
    '''房屋朝向'''
    houseOrientation = ''
    '''车位情况'''
    isParkingLot = False

    '''房屋建造时间'''
    houseCreateTime = 0



    def __init__(self):
        '''
        Constructor
        '''