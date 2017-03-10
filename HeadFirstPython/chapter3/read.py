#!/usr/bin/env python
# coding=utf-8

import os

try:
    data = open("sketch.txt")

    for each_line in data:
        # print(each_line,end='')
        # print(each_line.split(":"),end='')
        try:
            if (each_line.find(":") != -1):
                (role, line_spoken) = each_line.split(":",1)
                print(role,end='')
                print(" said:",end='')
                print(line_spoken,end='') 
            else:
                print(each_line,end='')
        except:
            pass
    data.close()
except:
    print('The data file is missing')
