# HRV from Empatica E4

Using the BVP file exported from the Empatica E4 band, this script uses the `peakutils`, and the Root Mean Square of the Successive Differences (RMSSD) to calculate the Heart Rate Variability, based on the next formula:

$\sqrt{\frac{1}{N-1}\sum_{i=1}^{N-1}((R - R)_{i+1}-(R - R)_i)^2}$


## Usage

Execute the script where you have all the data exported from your Empatica session.

```
python empaticaHRV.py
```

Code based on

* [EEGrunt](https://github.com/curiositry/EEGrunt)
* [Python Heart Rate Analysis Toolkit](https://github.com/paulvangentcom/heartrate_analysis_python)