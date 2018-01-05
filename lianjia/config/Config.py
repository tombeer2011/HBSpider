#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class Config(object):
    LIANJIA_DOMAIN = '''http://sh.lianjia.com'''
    LIANJIA_ERSHOUFANG_LIST = LIANJIA_DOMAIN + '''/ershoufang/d'''
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

