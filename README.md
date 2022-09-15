# CeBrA_Calibration

Created by Alex Conley

Requires HDTV by Jan Mayer

This is a program to energy calibrate CeBrA, get the relative width vs Energy and Efficiency of our array using calibration sources, either 60Co or 152Eu.

Note: Root spectrums are cebraE0_noCuts, this might need to be adjusted

60Co

	Run the get 60Co_get_fits.sh script using ./60Co_get_fits.sh

		-Adjust the path to run in the [echo "root open run_${RUNNO}_${RUNNO}.root" > fit.sh] line
		-only thing to adjust is maybe the threshold of the peak find
	
	
152Eu
A more complex process to get the plots becasuse there are a lot of peaks

	1) Run ./1_get_spectrum_ID.sh 
	2) Open a new terminal and run ./2_get_fits and input the fit ID of the calibration peaks
		-use PgUp/PgDn to naviagter through the different detectors
		- Calibration peaks can be ajusted in the script, i.e. add or remove whatever ones you want
	3) Run ./3_get_input_file.sh to get the input file that contains the run date and time (for efficiency)
	4) Run ./4_get_plots.sh to plot everything!
