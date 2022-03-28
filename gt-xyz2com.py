#!/usr/bin/env  python  
# Usage: gt-xyz2com.py file1.xyz file2.xyz ...

import sys, os

nprocs = "32"              # number of processors
mem = "96GB"               # memory threshold
method = "#B3LYP/gen opt " # method
chargemult = "0 1"         # charge and multiplicity

#==============
def fn ( inp, filename ):

 fd = open ( "%s.com"%filename, 'w' )

 print("%%NProcShared=%s"%nprocs, file=fd)
 print("%%Mem=%s"%mem, file=fd)
 print("%%chk=%s"%filename, file=fd)
 print("%s \n"%method, file=fd)
 print("Generated by gt-xyz2com.py \n", file=fd) 
 print("%s "%chargemult, file=fd)

 for line in inp[2:]:
      print (line, file=fd) 
 print ("\n\n", file=fd)
#=============

files = sys.argv[1:]
argc  = len(sys.argv)

if not files:
   string = sys.stdin
   fn ( string )
elif argc >= 2:
   for file in files:

     filename = str(os.path.splitext(file)[0]) 
     string = open ( file, 'r' ).readlines()
     fn ( string, filename )
else:
   print("Usage: %s [file]" % command )
