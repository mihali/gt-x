#!/usr/bin/perl -w
# Takes two arguments, the filename and cardinal number of STO


@element = ( 
  " H",
  " H",                        "He", 
  "Li", "Be", " B", " C", " N", " O", " F", "Ne", 
  "Na", "Mg", "Al", "Si", " P", " S", "Cl", "Ar",
  "Ca", "Sc", "Ti", " V", "Cr", "Mn", "Fe", "Co", 
        "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"
);

my @allines;
#my $file = $ARGV[0];
#my $number = $ARGV[1]; 
my ($file, $number) = @ARGV;

if (not defined $file) {
  die "Need file\n";
}
else{
open(MYFILE,"<$file") or die "Couldnt open file $!";
}
if (not defined $number) {
$number = 1000
}


my $j = 0;



while ( $lines=<MYFILE> )
{
        if ( $lines =~ m/Standard orientation:/ )
        {

          $j = $j + 1;

            if ( $j == $number || $number == 1000) {
                $i = 0;
                while ( $i++ < 4 )
                        {
                        $lines=<MYFILE>;
                        }

                @allines=();
                while ( ( $lines = <MYFILE> ) && !( $lines =~ m/---/ ) ) 
                        { 
                        my @line;
                        @line= split (/\s+/, $lines);
                        push (@allines, \@line);
                        }
           }

        }
}


                
                
foreach my $temp (@allines) {
        print "$element[$$temp[2]]  $$temp[4] $$temp[5] $$temp[6]\n";
}
