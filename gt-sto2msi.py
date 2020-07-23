#!/usr/bin/env  python3

import sys
element = [
  "H",
  "H",                        "He",
  "Li", "Be", " B", " C", " N", " O", " F", "Ne",
  "Na", "Mg", "Al", "Si", " P", " S", "Cl", "Ar",
  "Ca", "Sc", "Ti", " V", "Cr", "Mn", "Fe", "Co",
  "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr" ]


# using single bond radii www.iumsc.indiana.edu/helps/radii.html 
'''
radii = { 
  'H': 0.5,
  'D': 0.299,                                                 
  'He': 1.0,
  'Li': 0.5, 
  'Be': 1.06, 
  'B':  0.830, 
  'C':  0.767, 
  'N':  0.702, 
  'O':  1.0,  
  'F':  0.619, 
  'Ne': 1.0,
  'Na': 0.5,
  'Mg': 0.5,
  'Al': 1.0,
  'Si': 1.0, 
  'P':  1.088,
  'S':  1.052, 
  'Cl': 1.023,
  'Ar': 1.5    
  }
'''
radii = [ 
  0.5,
  0.299,                                                 
  1.0,
  0.5, 
  1.06, 
  0.830, 
  0.767, 
  0.702, 
  1.0,  
  0.619, 
  1.0,
  0.5,
  0.5,
  1.0,
  1.0, 
  1.088,
  1.052, 
  1.023,
  1.5    
 ]


# Function to print atoms

def PrintAtoms ( sto ):

  for row in sto:
    d = int(row[0]) + 1
    print (" (%s Atom " % d )
    print ("  (A C ACL \"%s %s\")  " % ( row[1], element[int(row[1])] ))
#      fprintf (output, "  (A C ACL \"%d %s\") \n", Z = (Z == 1) ? 0 : Z, element[Z]);
    print ("  (A D XYZ (%s %s %s)) " % (row[3], row[4], row[5]))
    print ("  (A I Id %s) " % d)
    print ("  (A I ZOrder %s)" % d)
    print (" ) ")


def PrintBonding (sto):
  
   newsto = sto.copy()
   i = 0
   for sto1 in sto:
     for sto2 in newsto:

       if sto1[0] > sto2[0]:
         distsq = (( float(sto1[3]) - float(sto2[3]) ) * ( float(sto1[3]) - float(sto2[3]) ) +
           ( float(sto1[4]) - float(sto2[4]) ) * ( float(sto1[4]) - float(sto2[4]) ) +
           ( float(sto1[5]) - float(sto2[5]) ) * ( float(sto1[5]) - float(sto2[5]) ))
         radsumsq = ( ( radii[int(sto1[1])] + radii[int(sto2[1])] ) *
           ( radii[int(sto1[1])] + radii[int(sto2[1])] ))   
         if radsumsq > distsq:
           print (" (%s Bond " % i )
           z1 = int(sto1[0]) + 1
           z2 = int(sto2[0]) + 1
           print ("  (A O Atom1 %s) " % z1 ) 
           print ("  (A O Atom2 %s) " % z2 )
           print (" ) ")
           i = i + 1

def grabSto ( fileln ):
  
  i = 0
  flag = 0
  sto = []

  for line in fileln:

    if "Standard orientation:" in line:
      sto = []
      flag = 1
    if flag == 1:
      i = i + 1
      if i < 6:
        continue
      elif "---" in line and i > 6 :
         i = 0
         flag = 0
      else:    
         sto.append( line.split() )

  return sto



print ("# MSI CERIUS2 DataModel File Version 3 0 ")
print ("(1 Model ")
print (" (A I Id 1)")
print (" (A C Label \"%s\")" % sys.argv[1] )

file = open ( sys.argv[1], 'r' )
sto = []
sto = grabSto ( file.readlines() ) 
PrintAtoms(sto)
PrintBonding(sto)

print (") ")





