'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.downloder.Downloader import Downloader
from lianjia.parser.Parser import Parser
from lianjia.storage.Storage import Storage

def main():
    dl = Downloader()
    dl.test()
    
    pa = Parser()
    pa.test()
    
    st = Storage()
    st.test()


main()