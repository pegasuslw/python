import requests
import urllib
import re
import random
from time import sleep

def main():    
    url='https://www.zhihu.com/question/22591304/followers' 
    headers={'User-agent:',"lw"} 
    i=1
    for x in xrange(20,100,20): 
        data={'start':'0','offset':str(x),'_xsrf':'a128464ef225a69348cef94c38f4e428'}
        content=requests.post(url,headers=headers,data=data,timeout=10).text
        print ('***********************************')
        print (content)

if __name__=='__main__':
    main()


