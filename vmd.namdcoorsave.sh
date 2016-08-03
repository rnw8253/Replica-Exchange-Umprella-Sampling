#!/bin/bash
i=6
while [ $i -le 60 ]
do
    j=`expr $i - 6`
    [ $i -le 9 ] && ip=0$i || ip=$i
    sed -e "s/YY/"$j"/"  NAMD.write.coor.tcl > test.in
    /Applications/VMD\ 1.9.2.app/Contents/MacOS/startup.command -dispdev text ../../close_start/equilibration/EAAAG.prmtop -rst7 ../../close_start/trajectories/REUS/EAAAG_$ip.centered.rst -e test.in 
    i=`expr $i + 1`
done



