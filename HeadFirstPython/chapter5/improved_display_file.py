#!/usr/bin/env python
# coding=utf-8

import os
import nestprint

def sanitize(time_string):
    if '-' in time_string:
        (mins,secs) = time_string.split('-',1)
        return mins + '.' + secs
    elif ':' in time_string:
        (mins,secs) = time_string.split(':',1)
        return mins + '.' + secs
    else: 
        return time_string

process = os.popen('ls *.txt')
output = process.read()
process.close()

output = output.strip()

output = output.split()

record_list = []
clean_record_list = []
sorted_clean_record_list = []
unique_record_list = []
try:
    for file_name in output:
        with open(file_name) as file:
            line = file.readline()   # 从文件中读取成绩
            record_list = line.strip().split(',')          # 将成绩转传承列表
            clean_record_list = [sanitize(each_word) for each_word in record_list] # 列表推导,对旧列表的数据进行转换
            #nestprint.print_lol(clean_record_list)  # 对转换后的列表进行排序
            sorted_clean_record_list = sorted(clean_record_list)
            print(file_name + ':' + str(sorted_clean_record_list))

            unique_record_list = []
            for each_item in sorted_clean_record_list:
                if each_item not in unique_record_list:
                    unique_record_list.append(each_item)
            #打印出前3个
            print(file_name + ':', end='');
            #lens = 3
            #if len(unique_record_list) < 3 :
            #    lens = len(unique_record_list)
            #for index in range(lens):
            #    print(unique_record_list[index] + " ", end='')
            #print()
            print(unique_record_list[0:3])

except IOError as err:
    print('process file ' +  file_name + ' error!')
    print('File error' + str(err))
    pass

