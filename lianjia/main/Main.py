#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.manager.Manager import Manager


def main():
    manager = Manager()
    manager.test()
    pass


main()