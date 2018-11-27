#!/usr/bin/env python

'''
Iftekhar Chowdhury
h.w. 8.2
'''
import os
import time

dir_to_watch = '.'
old = dict ([(f, None) for f in os.listdir (dir_to_watch)])
while True:
  time.sleep (5)  
  new = dict ([(f, None) for f in os.listdir (dir_to_watch)])
  added = ([f for f in new if not f in old])
  removed = ([f for f in old if not f in new])

  if added: print "Added file: ", ",".join(added)
  if removed: print "Removed file: ", ",".join (removed)
  old = new

    
 
