from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import time
from urllib.request import Request
req = Request("https://blog.csdn.net/csdngeeknews/article/details/145747333?spm=1000.2115.3001.5927", headers={'User-Agent': 'Mozilla/5.0'})
time.sleep(random.uniform(1,3))
pages=set()
random.seed(3)
def getInternallinks(bs0bj,includeURL):
    internallinks=[]
    for link in bs0bj.find_all("a",href=re.compile("^(/|.*"+includeURL+")")):
        if link.attrs is not None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks
def getExternallinks(bs0bj,excludeURL):
    externallinks=[]
    for link in bs0bj.find_all("a",href=re.compile("^(http|www)((?!"+excludeURL+").)*$")):
       if link.attrs is not None:
          if link.attrs['href'] not in externallinks:
             externallinks.append(link.attrs['href'])
    return externallinks
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts
def getRandomExternallink(startingPage):
    html=urlopen(startingPage)
    bs0bj=BeautifulSoup(html, 'html.parser')
    externallinks=getExternallinks(bs0bj,splitAddress(startingPage)[0])
    internallinks = getInternallinks(bs0bj, splitAddress(startingPage)[0])
    if len(externallinks)>1:
        if externallinks:
            a1=externallinks[random.randint(1,len(externallinks))-1]
            if a1 != "https://im.csdn.net/im/main.html?userName=weixin_47433511" and a1 !="https://blog.csdn.net/rank/list/force" and a1 !="https://www.csdn.net/vip" and a1 !="https://im.csdn.net/chat/2301_77554343":
             return a1
        else:
            return internallinks[random.randint(1,len(internallinks))-1]
    else:
        print("操作失败")
        return None
def followExternalOnly(startingSite):
    externallink=getRandomExternallink(startingSite)
    print("随机外链为："+externallink)
    followExternalOnly(externallink)
followExternalOnly("https://blog.csdn.net/csdngeeknews/article/details/145747333?spm=1000.2115.3001.5927")