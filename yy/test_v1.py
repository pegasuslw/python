#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import re
import sys

url_58_xiaoshou = 'http://xa.58.com/yewu/?PGTID=0d202408-001e-3247-3cc6-4f893bcf09f4&ClickID=2'

class Company_Info:
    name = ''   #公司名称
    url  = ''   # 包含公司详细信息的url
    from_site = ''   # 从哪个网站得到的公司信息，比如58, 51job
    def __init__(self,_name='',_url='',_from_site=''):
        self.name      = _name
        self.url       = _url
        self.from_site = _from_site

def download_url(url, max_try=2):
    try:
        html = urllib2.urlopen(url).read()
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
        return html



def write_url2file(file_name, html_content):
    with open(file_name,'w+') as file:
        file.write(html_content)

def read_file(file_name):
    with open(file_name,'r') as file:
        return file.read()


def get_58_single_company_url(info):
    result = re.findall('href=[\"|\'](.*?)[\"|\']',info)
    if len(result) == 1:
        return result[0]
    else:
        return ''

def get_58_single_company_name(info):
    result = re.findall('title=[\"|\'](.*?)[\"|\']',info)
    if len(result) == 1:
        return result[0]
    else:
        return ''

def get_58_single_company_info(info):  # info 包含了一个公司的信息，包含公司名称　和　公司详细信息的url
    company = Company_Info()

    result =  re.findall('<a(.*?)>(.*?)</a>',info)
    if len(result) == 1:
        #print 'start----------------'
        #for item in result[0]:
            #print item
        #print 'end----------------'
        #print len(result[0])
        
        if len(result[0]) == 2:
            company.name = result[0][1]

        company.url = get_58_single_company_url(result[0][0])
        company.name = get_58_single_company_name(result[0][0])
        #print '------------1---------------------'
        #print result[0][0]
        #print '------------2---------------------'
        #print result[0][1]
        #print isinstance(result[0][1],unicode)
        #print result[0].encode('UTF-8')
    return company


#html = download_url(url_58_xiaoshou)
#write_url2file('58_xiaoshou.html',html)
#html = read_file('58_xiaoshou.html')
#companys_html = re.findall('<dd class="w271"(.*?)</dd>',html)
#companys = []
#for item in companys_html:
#    company = get_58_single_company_info(item)
#    companys.append(company)


my_test_url = 'http://xa.58.com/yewu/pn%d/?PGTID=0d30364d-001e-34ff-e551-57e386e4f3d4&ClickID=3'

urls = []
for i in xrange(1,10,1):
    url = my_test_url % i
    urls.append(url)

def get_companys_from_58_url(url):  # return 一个列表，列表项是一个Company_Info对象
    html = download_url(url)
    companys_html = re.findall('<dd class="w271"(.*?)</dd>',html)
    companys = []
    for item in companys_html:
        company = get_58_single_company_info(item)
        if company.name:
            companys.append(company)

    return companys    #返回列表，每个项是Company_Info对象

def get_companys_from_58_urls(urls):
    companys = []
    for url in urls:
        print url
        companys.extend(get_companys_from_58_url(url))
    return companys
    

companys = get_companys_from_58_urls(urls)
print (len(companys))
for company in companys:
    #if isinstance(company, NoneType):
    #    break
    if isinstance(company, Company_Info):
        print(company.name + " url: " + company.url)

print (len(companys))
