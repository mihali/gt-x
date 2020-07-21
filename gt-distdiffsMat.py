#!/usr/bin/env python3

# Takes two Gaussian (g09) log files and finds the difference between the
# distance matrices.
# Uses 'zip' trick to compute the difference

import sys


###################################
# distance function takes file and 
# returns a rebuilt matrix 
##

def distances ( file, d ):

# Put the pertinent lines in a matrix

  flag = 0
  flines = file.readlines()
  lines = []
  for line2 in flines:
    if "Distance matrix (angstroms)" in line2:
       flag = 1
    elif line2.startswith("              "):
       continue
    elif line2.startswith(" Stoichiometry"):
       flag = 0
       break
    elif flag == 1:
       lines.append(line2.strip())

# Split the lines into tokens and then rebuild the matrix from the page-fitted format  

  counter = 0
  everything={}
  for line in lines:
    list1 = line.split()
    j = 2

    for x in list1[2:]:
      if float(x) > d:
         list1[j] = '0.0'
      j = j + 1

    if list1[0] in everything:
       everything[list1[0]].extend(list1[2:])
    else:
       everything [list1[0]] = list1 
       counter = counter + 1 
  
  returnable = []
  i = 0
  while i < counter:
    i = i + 1
    returnable.append (everything[str(i)][2:]) 
  
  return returnable
####################################

argc = len(sys.argv)

k=1
l=2
d=2.0 # default bond length cap

if argc == 2 or argc > 4:
   print ("Usage: %s [-bondlengthmax] file1 file2" % sys.argv[0] ) 
   exit()
elif sys.argv[1].startswith("-"):
   d=-float(sys.argv[1])
   k=2
   l=3

print ("Bond length cap is set to " + str(d)  )

file1 = open ( sys.argv[k], 'r' ) 
file2 = open ( sys.argv[l], 'r' )

A = distances ( file1, d )
B = distances ( file2, d )


count = 0 
for a in A:
   b = B[count]
   difference = []
   zip_object = zip(a, b)
   for list1_i, list2_i in zip_object:
      difference.append(float(list1_i)-float(list2_i))
   print(difference) 
   count = count +1  
