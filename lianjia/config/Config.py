#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''

import sys


reload(sys)
sys.setdefaultencoding("utf8")

class Config(object):
    '''主域名'''
    LIANJIA_DOMAIN = '''http://sh.lianjia.com'''
    '''房源列表url'''
    LIANJIA_ERSHOUFANG_LIST = LIANJIA_DOMAIN + '''/ershoufang/d'''
    '''每个房间的详细信息'''
    LIANJIA_ROOMS_DATAIL = LIANJIA_DOMAIN + '''/api/house/getCells.json?houseId={0}''' + '''&type=ershou'''
    '''开房记录链接'''
    LIANJIA_KANFANG_HISTORY = '''http://m.sh.lianjia.com/ershoufang/jilu/'''

    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

