#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.manager.Manager import Manager


urlList = []
'''爬取的页数'''
pageCount = 2

def main():
    manager = Manager()
    # manager.test()
    '''获取每个列表的所有详情页的url链接'''
    urlList = manager.getAllDetailLinks(pageCount)
    print (urlList)
    # for i in range(len(urlList)):
    #     for j in range(len(urlList[i])):
    #         manager.getDetailLinks()
    #         pass
    pass


main()