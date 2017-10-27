# HRV from Empatica E4

Using the BVP file exported from the Empatica E4 band, this script uses the `peakutils`, and the standard deviation of R-R intervals to calculate the Heart Rate Variability.

##Usage

Execute the script in the same folder you have all the data exported from your Empatica session.

```
python empaticaHRV.py
```

Code based on

* [EEGrunt](https://github.com/curiositry/EEGrunt)
* [Python Heart Rate Analysis Toolkit](https://github.com/paulvangentcom/heartrate_analysis_python)