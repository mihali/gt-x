#!/usr/bin/env  python  
# Description: Get archive of successful run and turn into human readable format.
# Usage: gt-parsearchive.py [ < file | file1 file2 .... ]

import sys

def fn (string):
 flag = 0
 linenew2=''
 for line in string:
   linenew = line.strip()
   if "1\\1\\" in linenew:
       linenew2 = linenew2 + linenew
       flag = 1
   elif "@" in linenew:
          linenew2 = linenew2 + linenew
          data=[]
          data=linenew2.split('\\')
          for line2 in data:
                  print (line2)
                  flag = 0
          linenew=''
          linenew2=''
   elif flag == 1:
       linenew2 = linenew2 + linenew

files = sys.argv[1:]
if not files:
   string = sys.stdin
   fn ( string )
else:
   for file in files:
     string = open ( file, 'r' ).readlines()
     fn ( string )
