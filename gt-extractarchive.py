#!/usr/bin/env  python  
# Description: Get archive of successful run.
# Usage: gt-extractarchive.py [ < file | file1 file2 .... ]

import sys

def fn (string ):
 flag = 0
 for line in string:
   linenew = line.strip()
   if "1\\1\\" in linenew:
       print(linenew)
       flag = 1
   elif "@" in linenew:
       print(linenew)
       flag = 0
   elif flag == 1:
       print(linenew)

files = sys.argv[1:]
if not files:
   string = sys.stdin
   fn ( string )
else:
   for file in files:
     string = open ( file, 'r' ).readlines()
     fn ( string )
