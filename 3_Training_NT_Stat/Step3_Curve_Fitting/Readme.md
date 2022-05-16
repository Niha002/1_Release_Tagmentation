### Aim: 
For the whole pan-genome ensemble curve fit the histogram. 

Integrate the fitted curve to get the CDF and generate the lookup table.

This lookup table will be used as model for prediction by linear interpolation.

     
### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* Un-binned "NI_all.txt" from step 2d pan genome ensemble 
* T0_final.mat 
* T0_Histogram.mat
* T0_func_fliplognorm.m

### Input: 
Histograms xdata and ydata "T0_Histogram.mat" for the pan-genome ensemble from step 2d 

### Run:
Just run the Script with the files in the directory

### Code:
1. Step 1 : load histogram
1. Step 2 : x-axis for plotting
1. Step 3 : initial stat parameters for estimation -> fliplognormal
1. Step 4 : lognormal is flipped as -ve tail on the other end
1. Step 5 : LSQCURVEFIT on the initial flip lognormal value
1. Step 6 : CDF intrgrating PDF
1. Step 7 : Plot functions (Histogram, PDF, CDF)
1. Step 8 : Save the Lookup table (x,y) = (Sequence score, CDF)


### Output: 
The expected output is 

* Image of PDF: Histogram and Actual Curve Fit 

  <img width="437" alt="image" src="https://user-images.githubusercontent.com/55808380/168493535-859687b2-4d28-4087-a979-44e629214f98.png">

* A matfile for the prediction for step 4 using T_Output_Lookuptable.mat 
