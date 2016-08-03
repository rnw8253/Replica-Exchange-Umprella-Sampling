#!/bin/bash

# sort the replicas
~/Desktop/NAMD/sortreplicas ../output/%s/EAAAG_com.job0 24 10

## run time_series.vmd analysis
#for i in {0..24}
#do
#   /Applications/VMD\ 1.9.2.app/Contents/MacOS/startup.command -dispdev text -e time_series.vmd -args $i 0
#   echo "`cat -n time_series/alanine_0_$i.anal`" > time_series/EAAAG_0_$i.anal
#done
#
## run WHAM analysis
#/Users/Ryan/Desktop/wham/wham/wham 7 20 100 0.01 298 0 meta PMF.out
