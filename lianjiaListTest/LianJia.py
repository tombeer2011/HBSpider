'''
Created on Jan 3, 2018

@author: hb
'''
import sys

reload(sys)
sys.setdefaultencoding("utf8")

import requests
import urllib2  
import time    
from bs4 import BeautifulSoup  
time.clock()  

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}
url = 'http://sh.lianjia.com/ershoufang/'
page=('d')
for i in range(1):  

    i=str(i)
    a=(url+page+i+'/')
    
    r=requests.get(url=a,headers=headers)
    html=r.content
#     url = 'http://sh.lianjia.com/ershoufang/d1'
#     page1 = urllib2.urlopen(a)  
    lj = BeautifulSoup(html,'html.parser') 
    # print(soup) 
    # for link in soup.find_all('div','houseInfo'):  
    #     context = link.get_text()  
    #     print(context)
    # for link in soup.find_all('div','totalPrice'):
    #     context = link.span.string
    #     print(context)

# <div class="info-col price-item main">
#                             <span class="total-price strong-num">695</span>
#                             <span class="unit"></span>
#                         </div>
    price=lj.find_all('span',attrs={'class':'total-price strong-num'})
    tp=[]
    for a in price:
        totalPrice=a.string
        tp.append(totalPrice)
#     print(tp)
    
    houseInfo=lj.find_all('span',attrs={'class':'info-col row1-text'})
    hi=[]
    for b in houseInfo:
        house=b.get_text().replace('\n','').replace('\t','')
        hi.append(house)
    
    houseInfoLoc = lj.find_all('span',attrs={'class':'info-col row2-text'})
    hil=[]
    for b in houseInfoLoc:
        house=b.get_text().replace('\n','').replace('\t','')
        hil.append(house)
#     print(hi)
    
    average_price = []
    houseAveragePrice = lj.find_all('span',attrs={'class':'info-col price-item minor'})
    for b in houseAveragePrice:
        house=b.get_text().replace('\n','').replace('\t','')
        average_price.append(house)
        
#     followInfo=lj.find_all('div',attrs={'class':'followInfo'})
#      
#     fi=[]
#     for c in followInfo:
#         follow=c.get_text()
#         fi.append(follow)
    
    import pandas as pd

    house=pd.DataFrame({'totalprice':tp,'houseinfo':hi,"houseInfoLoc":hil,"averagePrice":average_price})
    
    house.head()
    print(house.head())
    
    houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseinfo),
                                   columns=['xiaoqu','huxing'])
#     
    houseinfo_split.head()
#     print(houseinfo_split)
#     
#     house=pd.merge(house,houseinfo_split,right_index=True, left_index=True)
#     
#     house.head()
#     
#     followinfo_split = pd.DataFrame((x.split('/') for x in house.followinfo),index=house.index,columns=['guanzhu','daikan','fabu'])
#     
#     house=pd.merge(house,followinfo_split,right_index=True, left_index=True)
#     print(house)
    #     print(context)
print(time.clock())