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
import json

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
        return houseIndex[0]

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

    '''获取X室X厅X卫'''
    @staticmethod
    def getRoomsHalls(str):
        pattern = u'室|厅|卫'
        result = re.split(pattern,str)
        return result
        pass

    '''获取所在楼层和总层高'''
    @staticmethod
    def getFloor(str):
        pattern = u'/'
        result = []
        tmp = re.split(pattern,str)
        result.append(tmp[0])
        if(len(tmp)>1):
            result.append(ReUtils.getNumbericValue(tmp[1]))
        return result
        pass

    '''获取对象的json字符串形式'''
    @staticmethod
    def getObj2Json(obj):
        jsonStr = json.dumps(obj, ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return jsonStr
        pass
