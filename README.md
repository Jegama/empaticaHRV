# HRV from Empatica E4

Using the BVP file exported from the Empatica E4 band, this script uses the `peakutils`, and the Root Mean Square of the Successive Differences (RMSSD) to calculate the Heart Rate Variability, based on the next formula:

<img src="https://latex.codecogs.com/gif.latex?$$\sqrt{\frac{1}{N-1}\left(\sum_{i=1}^{N-1}\Big((R&space;-&space;R)_{i&plus;1}-(R&space;-&space;R)_i\Big)^2\right)}$$" title="$$\sqrt{\frac{1}{N-1}\left(\sum_{i=1}^{N-1}\Big((R - R)_{i+1}-(R - R)_i\Big)^2\right)}$$" />


## Usage

Execute the script where you have all the data exported from your Empatica session.

```
python empaticaHRV.py
```

Code based on

* [EEGrunt](https://github.com/curiositry/EEGrunt)
* [Python Heart Rate Analysis Toolkit](https://github.com/paulvangentcom/heartrate_analysis_python)