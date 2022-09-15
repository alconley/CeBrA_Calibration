root open run_10_10.root
root get cebraE0_noCuts
fit peakfind -t 0.5 -a
calibration position assign 0 1173.2280(30) 1 1332.492(4) 
fit list
calibration position list write -F run_10_detector_0_energycal.txt
fit delete 0-100
fit marker region set 1125 1240 
fit marker peak set 1173.2280
fit
fit store
fit clear
fit marker region set 1270 1400 
fit marker peak set 1332.49
fit
fit store
fit clear
fit show decomposition 0-100
fit list
fit write -F run_10_detector_0_fits.txt
q
root get cebraE1_noCuts
fit peakfind -t 0.5 -a
calibration position assign 0 1173.2280(30) 1 1332.492(4) 
fit list
calibration position list write -F run_10_detector_1_energycal.txt
fit delete 0-100
fit marker region set 1125 1240 
fit marker peak set 1173.2280
fit
fit store
fit clear
fit marker region set 1270 1400 
fit marker peak set 1332.49
fit
fit store
fit clear
fit show decomposition 0-100
fit list
fit write -F run_10_detector_1_fits.txt
q
root get cebraE2_noCuts
fit peakfind -t 0.5 -a
calibration position assign 0 1173.2280(30) 1 1332.492(4) 
fit list
calibration position list write -F run_10_detector_2_energycal.txt
fit delete 0-100
fit marker region set 1125 1240 
fit marker peak set 1173.2280
fit
fit store
fit clear
fit marker region set 1270 1400 
fit marker peak set 1332.49
fit
fit store
fit clear
fit show decomposition 0-100
fit list
fit write -F run_10_detector_2_fits.txt
q
root get cebraE3_noCuts
fit peakfind -t 0.5 -a
calibration position assign 0 1173.2280(30) 1 1332.492(4) 
fit list
calibration position list write -F run_10_detector_3_energycal.txt
fit delete 0-100
fit marker region set 1125 1240 
fit marker peak set 1173.2280
fit
fit store
fit clear
fit marker region set 1270 1400 
fit marker peak set 1332.49
fit
fit store
fit clear
fit show decomposition 0-100
fit list
fit write -F run_10_detector_3_fits.txt
q
root get cebraE4_noCuts
fit peakfind -t 0.5 -a
calibration position assign 0 1173.2280(30) 1 1332.492(4) 
fit list
calibration position list write -F run_10_detector_4_energycal.txt
fit delete 0-100
fit marker region set 1125 1240 
fit marker peak set 1173.2280
fit
fit store
fit clear
fit marker region set 1270 1400 
fit marker peak set 1332.49
fit
fit store
fit clear
fit show decomposition 0-100
fit list
fit write -F run_10_detector_4_fits.txt
q
