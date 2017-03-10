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

def get_data(file_name):
    #dic_value = {}
    try:
        with open(file_name) as file:
            times_list = file.readline().strip().split(",");
            #dic_value['name'] = list.pop()
            #dic_value['birthday'] = list.pop()
            #dic_value['times'] = list
            #return dic_value
            return ({'name':times_list.pop(0), 
                     'birthday':times_list.pop(0), 
                     'times':sorted(set([sanitize(t) for t in times_list]))[0:3]})
    except IOError as err:
        print("deal with " + file_name + " err:" +str(err) );
        return (None)

james = get_data("james.txt")
print(type(james))
print(james['name'] + "'s fast times:'" + str(james['times']) )

mikey = get_data("mikey.txt")
print(mikey['name'] + "'s fast times:'" + str(mikey['times']) )

juli  = get_data("julie.txt")
print(juli['name'] + "'s fast times:'" + str(juli['times']) )

sarah  = get_data("sarah.txt")
print(sarah['name'] + "'s fast times:'" + str(sarah['times']) )
