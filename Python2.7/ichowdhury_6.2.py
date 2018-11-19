#!/usr/bin/env python
#hw: 6.2
# Iftekhar Chowdhury


from config import conf

    
for domain_name in conf:
    
    print "domain :", domain_name ['domain']
    
    print "db_host:",domain_name['database']['host']
    print "db_port:",domain_name['database']['port']
    
    print "Plugins:"
    print " ",domain_name['plugins'][0]
    print " ",domain_name['plugins'][1]
    print
    


     


