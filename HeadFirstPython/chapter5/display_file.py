#!/usr/bin/env python
# coding=utf-8

def sanitize(time_string):
    if '-' in time_string:
        (mins,secs) = time_string.split('-',1)
        return mins + '.' + secs
    elif ':' in time_string:
        (mins,secs) = time_string.split(':',1)
        return mins + '.' + secs
    else: 
        return time_string

try:
    with open('james.txt') as file:
        data = file.readline()
        james = data.strip().split(',')
except FileNotFoundError as err:
    print(str(err))
try:
    with open('mikey.txt') as file:
        data = file.readline()
        mikey = data.strip().split(',')
except FileNotFoundError as err:
    print(str(err))

with open('julie.txt') as file:
    data = file.readline()
    julie = data.strip().split(',')

with open('sarah.txt') as file:
    data = file.readline()
    sarah = data.strip().split(',')

clean_james = []
clean_mikey = []
clean_julie = []
clean_sarah = []
if 'james' in locals():
    for each_word in james:
        clean_james.append(sanitize(each_word))
    print(sorted(clean_james))
if 'mikey' in locals():
    for each_word in mikey:
        clean_mikey.append(sanitize(each_word))
    print(sorted(clean_mikey))
if 'julie' in locals():
    for each_word in julie:
        clean_julie.append(sanitize(each_word))
    print(sorted(clean_julie))
if 'sarah' in locals():
    for each_word in sarah:
        clean_sarah.append(sanitize(each_word))
    print(sorted(clean_sarah))



