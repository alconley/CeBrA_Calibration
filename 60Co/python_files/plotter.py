import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


import input_file as inp


Activity = 74370 #activity on 152Eu Container in Bq
Half_life = 13.537 #years
lambda_days = np.log(2)/(Half_life*365.25)

OG_Date = dt.datetime(2017,3,17,12,0,0) #date on 152Eu Container
Today_Date = dt.datetime(inp.Run_Year,inp.Run_Month,inp.Run_Day,12,0,0)

Activity_Today = Activity * np.exp(-lambda_days * float((Today_Date-OG_Date).days))

Co60_energy = np.array([1173.2280,1332.492]) #in keV
Co60_intensity = np.array([99.850,99.9826]) #in %

Co60_dic = dict(zip(Co60_energy, Co60_intensity))

Run_Time = (inp.Run_Hour*3600) + (inp.Run_Minute*60) + (inp.Run_Seconds)


i=0
while i <= 4:  
       
       dict={}
       
       with open("./data_files/detector_" + str(i) + "_calibrated_data.txt") as f:
              stripped=[s.strip() for s in f]
              for line in stripped:
                     energy,energy_error,width,width_error,volume,volume_error=line.split()
                     top_err = float(energy)+10.0
                     bot_err = float(energy)-10.0
                     for key in Co60_dic:
                            if(key >= bot_err and key <= top_err):
                                   dict[key] = [float(energy), float(energy_error), float(width),
                                                float(width_error), float(volume), float(volume_error), Co60_dic[key]]
                                           
                     
                     Energy = []
                     Energy_Error = []
                     Width = []
                     Width_Error = []
                     Relative_Width = []
                     Relative_Width_Error = []                     
                     Efficiency = []
                     Efficiency_Error = []
                     Fit_Residual = []
                     for key in dict:
                            Energy.append(dict[key][0])
                            Energy_Error.append(dict[key][1])
                            Width.append(dict[key][2])
                            Width_Error.append(dict[key][3])
                            Relative_Width.append(dict[key][2]/dict[key][0]*100) #in % units
                            Relative_Width_Error.append( np.sqrt(float(dict[key][3]/dict[key][2])**2 + (dict[key][1]/dict[key][0])**2) * (dict[key][2]/dict[key][0]*100))
                            Efficiency.append(dict[key][4]/(dict[key][6]*Activity_Today*Run_Time*0.01)*100)
                            Efficiency_Error.append(dict[key][5]/dict[key][4]*dict[key][6])
                            Fit_Residual.append(key-dict[key][0])

                            
                                          
              if i == 0:              
                     det_0_dict = dict
                     Energy_det_0 = Energy
                     Energy_Error_det_0 = Energy_Error
                     Width_det_0 = Width
                     Width_Error_det_0 = Width_Error
                     Relative_Width_det_0 = Relative_Width
                     Relative_Width_Error_det_0 = Relative_Width_Error
                     Efficiency_det_0 = Efficiency 
                     Efficiency_Error_det_0 = Efficiency_Error
                     Fit_Residual_det_0 = Fit_Residual
                     
                     
              if i == 1:              
                     det_1_dict = dict
                     Energy_det_1 = Energy
                     Energy_Error_det_1 = Energy_Error
                     Width_det_1 = Width
                     Width_Error_det_1 = Width_Error
                     Relative_Width_det_1 = Relative_Width
                     Relative_Width_Error_det_1 = Relative_Width_Error
                     Efficiency_det_1 = Efficiency 
                     Efficiency_Error_det_1 = Efficiency_Error
                     Fit_Residual_det_1 = Fit_Residual
                     

              if i == 2:              
                     det_2 = dict
                     Energy_det_2 = Energy
                     Energy_Error_det_2 = Energy_Error
                     Width_det_2 = Width
                     Width_Error_det_2 = Width_Error
                     Relative_Width_det_2 = Relative_Width
                     Relative_Width_Error_det_2 = Relative_Width_Error
                     Efficiency_det_2 = Efficiency 
                     Efficiency_Error_det_2 = Efficiency_Error
                     Fit_Residual_det_2 = Fit_Residual
                     
              if i == 3:              
                     det_3 = dict
                     Energy_det_3 = Energy
                     Energy_Error_det_3 = Energy_Error
                     Width_det_3 = Width
                     Width_Error_det_3 = Width_Error
                     Relative_Width_det_3 = Relative_Width
                     Relative_Width_Error_det_3 = Relative_Width_Error
                     Efficiency_det_3 = Efficiency 
                     Efficiency_Error_det_3 = Efficiency_Error
                     Fit_Residual_det_3 = Fit_Residual
                     
              if i == 4:              
                     det_4 = dict
                     Energy_det_4 = Energy
                     Energy_Error_det_4 = Energy_Error
                     Width_det_4 = Width
                     Width_Error_det_4 = Width_Error
                     Relative_Width_det_4 = Relative_Width
                     Relative_Width_Error_det_4 = Relative_Width_Error
                     Efficiency_det_4 = Efficiency 
                     Efficiency_Error_det_4 = Efficiency_Error
                     Fit_Residual_det_4 = Fit_Residual
                                   
       i+=1

figuresize = (15,15)
fig = plt.figure(figsize=figuresize)
gs = fig.add_gridspec(5,4,top=0.995,bottom=0.045,left=0.025,right=0.995,hspace=0.0,wspace=0.125)
(ax00,ax01,ax02,ax03),(ax10,ax11,ax12,ax13),(ax20,ax21,ax22,ax23),(ax30,ax31,ax32,ax33),(ax40,ax41,ax42,ax43) = gs.subplots(sharex='col')

ax00.errorbar(Energy_det_0,Fit_Residual_det_0, yerr = Energy_Error_det_0, fmt='x', ecolor='red',capsize=2.0)
ax10.errorbar(Energy_det_1,Fit_Residual_det_1, yerr = Energy_Error_det_1, fmt='x', ecolor='red',capsize=2.0)
ax20.errorbar(Energy_det_2,Fit_Residual_det_2, yerr = Energy_Error_det_2, fmt='x', ecolor='red',capsize=2.0)
ax30.errorbar(Energy_det_3,Fit_Residual_det_3, yerr = Energy_Error_det_3, fmt='x', ecolor='red',capsize=2.0)
ax40.errorbar(Energy_det_4,Fit_Residual_det_4, yerr = Energy_Error_det_4, fmt='x', ecolor='red',capsize=2.0)

ax01.errorbar(Energy_det_0,Efficiency_det_0, yerr = Efficiency_Error_det_0, fmt='x', ecolor='red',capsize=2.0)
ax11.errorbar(Energy_det_1,Efficiency_det_1, yerr = Efficiency_Error_det_1, fmt='x', ecolor='red',capsize=2.0)
ax21.errorbar(Energy_det_2,Efficiency_det_2, yerr = Efficiency_Error_det_2, fmt='x', ecolor='red',capsize=2.0)
ax31.errorbar(Energy_det_3,Efficiency_det_3, yerr = Efficiency_Error_det_3, fmt='x', ecolor='red',capsize=2.0)
ax41.errorbar(Energy_det_4,Efficiency_det_4, yerr = Efficiency_Error_det_4, fmt='x', ecolor='red',capsize=2.0)

ax02.errorbar(Energy_det_0,Relative_Width_det_0, yerr = Relative_Width_Error_det_0, fmt='x', ecolor='red',capsize=2.0)
ax12.errorbar(Energy_det_1,Relative_Width_det_1, yerr = Relative_Width_Error_det_1, fmt='x', ecolor='red',capsize=2.0)
ax22.errorbar(Energy_det_2,Relative_Width_det_2, yerr = Relative_Width_Error_det_2, fmt='x', ecolor='red',capsize=2.0)
ax32.errorbar(Energy_det_3,Relative_Width_det_3, yerr = Relative_Width_Error_det_3, fmt='x', ecolor='red',capsize=2.0)
ax42.errorbar(Energy_det_4,Relative_Width_det_4, yerr = Relative_Width_Error_det_4, fmt='x', ecolor='red',capsize=2.0)

ax03.errorbar(Energy_det_0,Width_det_0, yerr = Width_Error_det_0, fmt='x', ecolor='red',capsize=2.0)
ax13.errorbar(Energy_det_1,Width_det_1, yerr = Width_Error_det_1, fmt='x', ecolor='red',capsize=2.0)
ax23.errorbar(Energy_det_2,Width_det_2, yerr = Width_Error_det_2, fmt='x', ecolor='red',capsize=2.0)
ax33.errorbar(Energy_det_3,Width_det_3, yerr = Width_Error_det_3, fmt='x', ecolor='red',capsize=2.0)
ax43.errorbar(Energy_det_4,Width_det_4, yerr = Width_Error_det_4, fmt='x', ecolor='red',capsize=2.0)

ax40.set_xlabel('Energy [keV]')
ax41.set_xlabel('Energy [keV]')
ax42.set_xlabel('Energy [keV]')
ax43.set_xlabel('Energy [keV]')

ax20.set_ylabel('Residual [keV]')
ax21.set_ylabel('Efficiency [%]')
ax22.set_ylabel('Relative Width [%]')
ax23.set_ylabel('FWHM [keV]')

minor_length = 2
major_length = 7

#PAIN
#I AM SO SORRY FOR MY SINS
ax00.minorticks_on()
ax10.minorticks_on()
ax20.minorticks_on()
ax30.minorticks_on()
ax40.minorticks_on()
ax01.minorticks_on()
ax11.minorticks_on()
ax21.minorticks_on()
ax31.minorticks_on()
ax41.minorticks_on()
ax02.minorticks_on()
ax12.minorticks_on()
ax22.minorticks_on()
ax32.minorticks_on()
ax42.minorticks_on()
ax03.minorticks_on()
ax13.minorticks_on()
ax23.minorticks_on()
ax33.minorticks_on()
ax43.minorticks_on()


ax00.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax10.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax20.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax30.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax40.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax01.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax11.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax21.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax31.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax41.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax02.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax12.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax22.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax32.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax42.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax03.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax13.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax23.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax33.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)
ax43.tick_params(axis='both',which='minor',direction='in',top=True,right=True,left=True,bottom=True,length=minor_length)

ax00.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax10.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax20.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax30.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax40.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax01.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax11.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax21.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax31.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax41.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax02.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax12.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax22.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax32.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax42.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax03.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax13.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax23.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax33.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)
ax43.tick_params(axis='both',which='major',direction='in',top=True,right=True,left=True,bottom=True,length=major_length)


        
plt.show()
        

