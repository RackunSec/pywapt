#!/usr/bin/env python
# 2019 Douglas Berdeaux
#
# :wq
import sys
import re
import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

def usage():
    print "\nComment Scrape\n2019 - WeakNet Labs\n"
    print "Usage: ./comment_scrape.py URL\n"
if (len(sys.argv)<2):
    usage()
    sys.exit()
else:
    print "\nFetching: "+sys.argv[1]+"\n"
    req_data = requests.get(sys.argv[1], stream=True)
    code_count = 0
    mlc = 0
    for code in req_data.iter_lines():
        if (mlc == 1): # we are in a multi-line comment
            if(re.match(".*-->",code) or re.match(".*\*/\s?$",code)): # end of multi-line comment
                print "Line "+str(code_count)+": "+code.rstrip()
                mlc = 0 # reset, exit the multi-line comment
            else:
                print "Line "+str(code_count)+": "+code.rstrip()
        if (re.match(".*<!--",code)
            or re.match("^\s+//",code)
            or re.match(".*/\*",code)):

            if(re.match(".*<!--\s?$",code) or re.match(".*/\*\s?$",code)):
                print "Line "+str(code_count)+": "+code.rstrip()
                mlc = 1 # Multi line comment token
            else:
                print "Line "+str(code_count) + ": " +code.rstrip()
        code_count += 1
    print "\n"
