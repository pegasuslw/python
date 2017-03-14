#!/usr/bin/env python
# coding=utf-8

import  urllib2
import re
import urlparse

exam1_url='http://www.heibanke.com/lesson/crawler_ex00/'
exam2_url='http://www.heibanke.com/lesson/crawler_ex01/'

'''<h3>你需要在网址后输入数字99039</h3>'''
def exam1_callback(url,html):
    result = re.findall('<h3>.*([\d]{5}).*</h3>',html)
    if len(result) == 1:
        tmp_url = urlparse.urljoin(exam1_url,result[0])
        print(tmp_url)
        download_url(tmp_url)
    else:
        print ('len is not 1 when found (你需要在网址后输入数字,)  url :' + url )
        print ('len:' + str(len(result)))
        print (html)
        return
def exam2_callback(url,html):
    result = re.findall('<h3>.*([\d]{5}).*</h3>',html)
    if len(result) == 1:
        tmp_url = urlparse.urljoin(exam1_url,result[0])
        print(tmp_url)
        download_url(tmp_url)
    else:
        print ('len is not 1 when found (你需要在网址后输入数字,)  url :' + url )
        print ('len:' + str(len(result)))
        print (html)
        return        
    
def download_url(url, max_try=2, user_agent='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0', call_back=exam1_callback,post_data=None):
    header = {'User-Agent':user_agent}
    if post_data:
        request = urllib2.Request(url,data=post_data,headers=header)  
    else:
        request = urllib2.Request(url,headers=header)    
    
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as err:
        if hasattr(err,'code'):
            if err.code > 500 and err.code < 600:
                if max_try > 0:
                    download_url(url,max_try-1)
            else:
                print ("URLError:" + err.code)
    if html is None:
        return None
    else:
        if call_back:
            call_back(url,html)
        return html

if __name__ == '__main__':
    print("hello")
    html = download_url(exam1_url)
    #print(html)


