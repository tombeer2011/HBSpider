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

    def getNumeric(self,string):
        pattern = re.compile(r'\d+')
        houseIndex = re.findall(pattern, string)
        return houseIndex