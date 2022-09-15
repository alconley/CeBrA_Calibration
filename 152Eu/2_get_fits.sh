#!/bin/bash


read -p "Please enter the run number again: " RUNNO

touch fit.sh
chmod +x fit.sh
echo "root open run_${RUNNO}_${RUNNO}.root" > fit.sh

n=0
while [ $n -le 4 ]
do
        echo "root get cebraE${n}_noCuts" >> fit.sh
        echo "fit peakfind -t 0.009 -a" >> fit.sh
        echo "Peak ID# for spectrum $n"
        
        read -p "121.78 keV peak ID#: " ID1
        read -p "244.69 keV peak ID#: " ID2
        read -p "344.27 keV peak ID#: " ID3
        read -p "778.90 keV peak ID#: " ID4
        read -p "964.07 keV peak ID#: " ID5
        read -p "1408.0 keV peak ID#: " ID6

        # $ID1 121.78170(30) $ID2 244.6974(8) $ID3 344.2785(12) $ID4 778.9045(24) $ID5 964.072(18) $ID6 1408.0130(30)

     

        echo "calibration position assign $ID1 121.78170(30) $ID2 244.6974(8) $ID3 344.2785(12) $ID4 778.9045(24) $ID5 964.072(18) $ID6 1408.0130(30)" >> fit.sh
        echo "fit position map Eu152.map" >> fit.sh
        echo "fit list" >> fit.sh
        echo "calibration position list write -F run_${RUNNO}_detector_${n}_energycal.txt" >> fit.sh
        echo "fit delete 0-100" >> fit.sh

        # 121.7817 keV peak
        echo "fit marker region set 100 140 " >> fit.sh
        echo "fit marker peak set 121.7817" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 244.6974 keV peak
        echo "fit marker region set 225 270" >> fit.sh
        echo "fit marker peak set 244.6974" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 344.278 keV peak" 
        echo "fit marker region set 310 380" >> fit.sh
        echo "fit marker peak set 344.278" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 411.116 keV peak
        # 443.965 keV peak
        echo "fit marker region set 387 470" >> fit.sh
        echo "fit marker peak set 411.116 443.965" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 778.904   keV peak"
        echo "fit marker region set 730 830" >> fit.sh
        echo "fit marker peak set 778.904" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 867.380   keV peak
        echo "fit marker region set 820 920" >> fit.sh
        echo "fit marker peak set 867.380" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 964.07    keV peak
        echo "fit marker region set 920 1040" >> fit.sh
        echo "fit marker peak set 964.07" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 1085.83   keV peak
        # 1112.076  keV peak  
        echo "fit marker region set 1040 1175" >> fit.sh
        echo "fit marker peak set 1085.83 1112.076" >> fit.sh
        echo "fit" >> fit.sh
        echo "fit store" >> fit.sh
        echo "fit clear" >> fit.sh

        # 1212.948  keV peak
        # 1299.142  keV peak

        # 1408.013  keV peak" >> fit.sh
        echo "fit marker region set 1345 1475" >> fit.sh
        echo "fit marker peak set 1409.013" >> fit.sh
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

 
