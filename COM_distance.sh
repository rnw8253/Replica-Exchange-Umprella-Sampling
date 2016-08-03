i=0
while [ $i -le 24 ]
do
    j=`expr $i + 16`
    sed -e "s/XX/"$i"/g" -e "s/YY/"$j"/g" COM_distance.cfg  > test.cfg
    python COM_distance.py test.cfg
    echo "`cat -n time_series/EAAAG.wind$j.REUS.dat`" > time_series/EAAAG.wind$j.REUS.dat
    i=`expr $i + 1`

done
