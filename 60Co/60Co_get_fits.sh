#!/bin/bash


read -p "Please enter the run number: " RUNNO
 

touch fit.sh
chmod +x fit.sh
echo "root open run_${RUNNO}_${RUNNO}.root" > fit.sh

n=0
while [ $n -le 4 ]
do
        echo "root get cebraE${n}_noCuts" >> fit.sh
        echo "fit peakfind -t 0.5 -a" >> fit.sh

        echo "calibration position assign 0 1173.2280(30) 1 1332.492(4) " >> fit.sh
        echo "fit list" >> fit.sh
        echo "calibration position list write -F run_${RUNNO}_detector_${n}_energycal.txt" >> fit.sh
        echo "fit delete 0-100" >> fit.sh

        # 1173.23 keV peak
        echo "fit marker region set 1125 1240 " >> fit.sh
        echo "fit marker peak set 1173.2280" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 1332.49 keV peak
        echo "fit marker region set 1270 1400 " >> fit.sh
        echo "fit marker peak set 1332.49" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh
       

        echo "fit show decomposition 0-100" >> fit.sh
        echo "fit list" >> fit.sh

        echo "fit write -F run_${RUNNO}_detector_${n}_fits.txt" >> fit.sh
        
        (( n++ ))
done

mv fit.sh ./hdtv_input_files/

hdtv -b ./hdtv_input_files/fit.sh

 
