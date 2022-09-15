#!/bin/bash


read -p "Please enter the run number: " RUNNO

touch open_root_file.sh
chmod +x open_root_file.sh
echo "root open run_${RUNNO}_${RUNNO}.root" > open_root_file.sh

for (( n=0; n<=4; n++))
do
    if (($n==0))
    then 
        echo "root get cebraE${n}_noCuts" >> open_root_file.sh
        echo "fit peakfind -t 0.009 -a" >> open_root_file.sh
    elif (($n==1)) 
    then 
        echo "root get cebraE${n}_noCuts" >> open_root_file.sh
        echo "fit peakfind -t 0.009 -a" >> open_root_file.sh
    elif (($n==2)) 
    then 
        echo "root get cebraE${n}_noCuts" >> open_root_file.sh
        echo "fit peakfind -t 0.009 -a" >> open_root_file.sh
    elif (($n==3)) 
    then 
        echo "root get cebraE${n}_noCuts" >> open_root_file.sh
        echo "fit peakfind -t 0.009 -a" >> open_root_file.sh
    elif (($n==4)) 
    then 
        echo "root get cebraE${n}_noCuts" >> open_root_file.sh
        echo "fit peakfind -t 0.009 -a" >> open_root_file.sh
    fi
        
done

mv open_root_file.sh ./hdtv_input_files/

hdtv -b ./hdtv_input_files/open_root_file.sh

 
