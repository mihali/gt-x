# gt-x
Gaussian logfile and inputfile tools

These are various short scripts to aid the analyses of Gaussian (gNN) output files. 

- **gt-distdiffsMat.py** - Compute change in distances between atoms from two log files. Makes use of the differences matrices.

- **gt-logn2com.pl** - Get the nth or last Standard Orientation from a log file and output a cartesian matrix for gNN input.

- **gt-parsearchive.py** - Make the archive output of a successful optimization run easier to read.

- **gt-sto2msi.py** - Create a Cerius 2.0 formatted file from the last Standard Orientation of a log file. 

- **gt-xyz2com.py** - Create Gaussian input file from xyz files. (This will be useful for the hydrocycler.)
