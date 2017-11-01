

######################################################################### 
#                                                                       #
#                       Jesus Garcia-Mancilla                           #
#                            Scrapworks                                 #
#                           October 2017                                #
#                                                                       #
#########################################################################

import pandas as pd
import numpy as np
import peakutils
import math, sys

print('\nStart')

def bvpPeaks(signal):
    cb = np.array(signal)
    x = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=0.1)
    y = []
    i = 0
    while (i < (len(x)-1)):
        if x[i+1] - x[i] < 15:
            y.append(x[i])
            x = np.delete(x, i+1)
        else:
            y.append(x[i])
        i += 1
    return y

def getRRI(signal, start, sample_rate):
    peakIDX = bvpPeaks(signal)
    spr = 1 / sample_rate # seconds between readings
    start_time = float(start)
    timestamp = [start_time, (peakIDX[0] * spr) + start_time ] 
    ibi = [0, 0]
    for i in range(1, len(peakIDX)):
        timestamp.append(peakIDX[i] * spr + start_time)
        ibi.append((peakIDX[i] - peakIDX[i-1]) * spr)

    df = pd.DataFrame({'Timestamp': timestamp, 'IBI': ibi})
    return df

def getHRV(data, avg_heart_rate):
    rri = np.array(data['IBI']) * 1000
    RR_list = rri.tolist()
    #RR_diff = []
    RR_sqdiff = []
    RR_diff_timestamp = []
    cnt = 2
    while (cnt < (len(RR_list)-1)): 
        #RR_diff.append(abs(RR_list[cnt+1] - RR_list[cnt])) 
        RR_sqdiff.append(math.pow(RR_list[cnt+1] - RR_list[cnt], 2)) 
        RR_diff_timestamp.append(data['Timestamp'][cnt])
        cnt += 1
    hrv_window_length = 10
    window_length_samples = int(hrv_window_length*(avg_heart_rate/60))
    #SDNN = []
    RMSSD = []
    index = 1
    for val in RR_sqdiff:
        if index < int(window_length_samples):
            #SDNNchunk = RR_diff[:index:]
            RMSSDchunk = RR_sqdiff[:index:]
        else:
            #SDNNchunk = RR_diff[(index-window_length_samples):index:]
            RMSSDchunk = RR_sqdiff[(index-window_length_samples):index:]
        #SDNN.append(np.std(SDNNchunk))
        RMSSD.append(math.sqrt(np.std(RMSSDchunk)))
        index += 1
    dt = np.dtype('Float64')
    #SDNN = np.array(SDNN, dtype=dt)
    RMSSD = np.array(RMSSD, dtype=dt)
    df = pd.DataFrame({'Timestamp': RR_diff_timestamp, 'HRV': RMSSD})
    return df

BVP_DF = pd.read_csv('BVP.csv')
HR_DF = pd.read_csv('HR.csv')

column = list(HR_DF)[0]
temp = HR_DF.drop(0, axis = 0)
HR = temp[column]
HR = HR.tolist()

column2 = list(BVP_DF)[0]
sample_rate = BVP_DF[column2][0]
temp = BVP_DF.drop(0, axis = 0)
temp['spData'] = 0
temp.loc[temp[column2] > 0, 'spData'] = temp[column2]
signal = temp['spData'].tolist()

RRI_DF = getRRI(signal, column2, sample_rate)
HRV_DF = getHRV(RRI_DF, np.mean(HR))

HRV_DF.to_csv('HRV.csv', index=False)

print('\n    Done, saved as: HRV.csv\n')

