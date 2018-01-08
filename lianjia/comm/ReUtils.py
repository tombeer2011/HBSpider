#encoding: utf-8
'''
Created on Jan 5, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

import re

class ReUtils(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    '''通过正则获取字符串中的数字'''
    @staticmethod
    def getNumeric(string):
        pattern = re.compile(r'\d+')
        houseIndex = re.findall(pattern, string)
        return houseIndex