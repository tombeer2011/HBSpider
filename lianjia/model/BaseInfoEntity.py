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

    def __init__(self):
        '''
        Constructor
        '''
        '''房屋户型'''
        self.houseTypeRoomNum = 0
        self.houseTypeHallNum = 0
        self.houseTypeBathNum = 0

        '''配备电梯'''
        self.lift = ''
        ''''''

        '''建筑面积'''
        self.houseArea = 0.0
        '''供暖方式'''
        self.heatingMethod = ''
        '''所在楼层'''
        self.houseFloor = ''
        '''总共层高'''
        self.houseTotalFloors = -1
        '''装修情况'''
        self.houseDecorate = ''
        '''房屋朝向'''
        self.houseOrientation = ''
        '''车位情况'''
        self.isParkingLot = False

        '''房屋建造时间'''
        self.houseCreateTime = 0

        # def __repr__(self):
        #     return repr((self.houseTypeRoomNum, self.houseTypeHallNum, self.houseTypeBathNum, self.lift,
        #                  self.houseArea,self.heatingMethod,self.houseFloor,self.houseTotalFloors,self.houseDecorate,
        #                  self.houseOrientation,self.isParkingLot,self.houseCreateTime))