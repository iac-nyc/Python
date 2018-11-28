#!/usr/bin/env python

'''
Iftekhar Chowdhury
h.w. 8.3
'''

import sys
import os

dictname = {}


root_dir = '/Users'
files = os.listdir(root_dir)
#filename = sys.argv[1]


for root, dirs, files in os.walk(root_dir):
    for filename in files:
        f_file = os.path.join(filename)
        if os.path.isfile(f_file):
            bytesize = os.path.getsize(f_file)
            dictname[filename] = bytesize
         
sorted_dict = sorted(dictname, key = dictname.get)
#print sorted_dict
for bytesize in sorted_dict[0:5]:
          
    print "{}   {}".format(f_file, bytesize)


