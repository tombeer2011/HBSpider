#encoding: utf-8
'''
Created on Jan 4, 2018

@author: hb
'''
import sys


reload(sys)
sys.setdefaultencoding("utf8")

from lianjia.manager.Manager import Manager
import json

urlList = []
'''爬取的页数'''
pageCount = 1

def main():
    manager = Manager()
    # manager.test()
    '''获取每个列表的所有详情页的url链接'''
    # urlList = manager.getAllDetailLinks(pageCount)
    # print (urlList)

    # for i in range(len(urlList)):
    #     for j in range(len(urlList[i])):
    #         manager.getDetailHtml(urlList[i][j])
    #         pass

    viewHouseHistory = manager.getViewHouseHistory('''http://m.sh.lianjia.com/ershoufang/jilu/4591094.html''')

    tmp = manager.getDetailHtml('''http://sh.lianjia.com/ershoufang/sh4591094.html''')
    # myClassDict = tmp.__dict__
    # print(myClassDict)
    # myClassJson = json.dumps(myClassDict)
    # print(myClassJson)



    pass


main()