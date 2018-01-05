#encoding: utf-8
'''
Created on Jan 5, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.downloder.Downloader import Downloader
from lianjia.parser.Parser import Parser
from lianjia.storage.Storage import Storage

class Manager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def test(self):
        dl = Downloader()
        dl.test()
    
        pa = Parser()
        pa.test()
    
        st = Storage()
        st.test()