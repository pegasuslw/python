#!/usr/bin/env python
# coding=utf-8

#import urllib.request
import urllib2
import re
from urllib2 import Request, urlopen, URLError, HTTPError

#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#httpsHandler = urllib2.HTTPHandler(debuglevel=1)
#opener = urllib2.build_opener(httpHandler, httpsHandler)
#urllib2.install_opener(opener)

#req = urllib2.Request('http://www.baidu.com');
req = urllib2.Request('http://xa.58.com/yewu/pn2/?PGTID=0d30364d-001e-32ef-7a1c-98d217c1f4b7&ClickID=3');
try:
    response = urllib2.urlopen(req)
    html = response.read()
    with open('./58_销售.html','w') as test_file:
        test_file.write(html)
    #match1 = re.match("\<dd.*\>.*\<\/dd\>",html)
    #print(html)
    b = re.compile(r".*<dd.*>.*</dd>.*")
    m = b.match(html)
    
    #pattern = re.compile(r'hello')
    #m = pattern.match('hello world!')
    #b = re.compile(r"\d+\.\d*") 
    #m = b.match('3.1415')
    if m:
        print(m.group())
    else:
        print("not match")


        
    #print(html)
#    print response.info()
#    print response.geturl()
#except HTTPError as err:
#    print(err.code)
except URLError as err:
    print(err.reason)

