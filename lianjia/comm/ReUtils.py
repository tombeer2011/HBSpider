#encoding: utf-8
'''
Created on Jan 5, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

import re
import string
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

    '''去除首尾回车和换行符'''
    @staticmethod
    def trimFLEnter(string):
        string = string.strip("""\n\r\t""")
        return string
        pass

    '''获取中间有多个换行符的字符串'''
    @staticmethod
    def replacEnter(str):
        tmpList = str.split('\n')
        result = []
        for i in range(len(tmpList)):
            tmp = tmpList[i].strip(string.punctuation).strip()
            if(tmp != u'\n' and tmp != u'' and tmp != '\r' and tmp != '\t'):
                result.append(tmp)
        return result
        pass

    '''获取浮点数或者正整数'''
    @staticmethod
    def getNumbericValue(str):
        pattern = re.compile(r'((^[0-9]*$))|(^(-?\d+)(\.\d+)?)')
        value = re.match(pattern,str)
        if(value):
            return value.group()
        else:
            return -1
        pass