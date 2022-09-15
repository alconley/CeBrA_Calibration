#!/bin/bash

echo "This is a script that will create a python file with the date and the time of the run"


touch input_file.py
chmod +x input_file.py

read -p "Please enter the run number: " RUNNO
echo "Run_Num = $RUNNO" > input_file.py

read -p "Please enter the year of run_$RUNNO : " YEAR
echo "Run_Year = $YEAR" >> input_file.py

read -p "Please enter the month of run_$RUNNO : " MONTH
echo "Run_Month = $MONTH" >> input_file.py

read -p "Please enter the day of run_$RUNNO : " DAY
echo "Run_Day = $DAY" >> input_file.py

read -p "How many hours was run_$RUNNO : " HOUR
echo "Run_Hour = $HOUR" >> input_file.py

read -p "How many minutes was run_$RUNNO : " MINUTE
echo "Run_Minute = $MINUTE" >> input_file.py

read -p "How many seconds was run_$RUNNO : " SECONDS
echo "Run_Seconds = $SECONDS" >> input_file.py

mv input_file.py ./python_files/









