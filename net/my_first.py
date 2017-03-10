#!/usr/bin/env python
# coding=utf-8


import urllib
import urllib2

from urllib2 import Request,urlopen,HTTPError, URLError

test_url='https://tieba.baidu.com/p/4977181527?pn='

def download_tieba(url,start, end):
    try:
        for num in xrange(start,end+1):
            req = urllib2.Request(url+str(num))
            rep = urllib2.urlopen(req)
            content = rep.read()

            file_name = str(num) + ".html"
            with open("./"+file_name,"w+") as file:
                file.write(content);
    except HTTPError as err:
        print err.code
        pass
    except URLError as err:
        print err.reason
        pass
    except IOError as err:
        print str(err)
        pass


download_tieba(test_url,1,10)
