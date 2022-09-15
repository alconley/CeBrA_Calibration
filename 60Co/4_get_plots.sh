#!/bin/bash

read -p "Please enter the run number one last time: " RUNNO

mkdir Run_Data/run_$RUNNO

mkdir ./python_files/fits
mv *fits.txt ./python_files/fits 

mkdir Run_Data/run_$RUNNO/energy_cal
mv *energycal.txt ./Run_Data/run_$RUNNO/energy_cal

cd ./python_files/

python3 xml_handle_cebra.py 

mv analyzed_fits data_files ../Run_Data/run_$RUNNO/
cp plotter.py input_file.py ../Run_Data/run_$RUNNO/
rm -r fits

cd ../Run_Data/run_$RUNNO/

python3 plotter.py




