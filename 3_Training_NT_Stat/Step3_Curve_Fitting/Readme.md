### Aim: 
Makes a sequence logo to see sequence biases in Tn5 region activity and PDF for each bins, where each sequence is 23bp(7:16).

Training the input data from the whole pan genome ensemble from step 2c and 2d.

Run the whole un-binned genome(pan-genome ensemble) profile and curve fit the histogram forms the histogram. 

Integrate the fitted curve to get the CDF and generate the lookup table.

     
### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* T0_func_seqlogo.m
* Binned files from step 2d pan genome ensemble 
* T0_final.mat 
* T0_Histogram.mat
* T0_func_fliplognorm.m

### Input: 
Use the demo file in this directory which looks like
> TGGAGTTTCCCCAGGAGGTCGAC
>
> GCGCCGGGTTACTGCCTGACGGA
>           
>.         ...
>
> TCGCTGATCTCCAGGGTCAGGTC
>
> GCTCGGTGCACCGGTGTTCGAGC

### Run:
>Enter sequence-file name: Demo.txt 
>
>File contains #x sequences
>
>Enforce motif symmetry: Y

### Code:
1. Step 1 : Extracts first Subseq_length nucleotides from each read
1. Step 2 : Concatenates each subsequence basecount function expects a single string
1. Step 3 : Compute base-call stats (determine ATGC percentages)
1. Step 4 : Generate base-call stats output
1. Step 5 : Generate profile, positional information matrix, and alignment score
1. Step 6 : Fit score distribution to Gaussian along with counts(histogram)
1. Step 7 : Save EVD Parameters and scoring matrix to file

1. Step 8 : x-axis for plotting
1. Step 9 : initial stat parameters for estimation -> fliplognormal
1. Step 10 : lognormal is flipped as -ve tail on the other end
1. Step 11 : LSQCURVEFIT on the initial flip lognormal value
1. Step 12 : CDF intrgrating PDF
1. Step 13 : Plot functions (Histogram, PDF, CDF)

### Output: 
The expected output is 

* Image of PDF: Histogram and Actual Curve Fit 

  <img width="437" alt="image" src="https://user-images.githubusercontent.com/55808380/168493535-859687b2-4d28-4087-a979-44e629214f98.png">

* A matfile for the prediction for step 4 using Lookup_table_cdf.mat 
