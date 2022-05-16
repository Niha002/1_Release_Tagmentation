### Aim: 
Makes a sequence logo to see sequence biases in Tn5 region activity and PDF for each bins, where each sequence is 23bp(7:16).

Training the input data from the whole pan genome ensemble from step 2c and 2d.

Run the whole un-binned genome(pan-genome ensemble) first and run the binned genome (increments of 5)
     
### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* A,T,G,C image file .png
* T0_func_seqlogo.m
* Binned files from step 2c/2d pan genome ensemble 

### Input: 
Use the demo file in this directory which looks like
> TTTAAATAAATAATATAAATTAC
>
> TTATTTAATATAAAGTAAAATAA
>           
>.         ...
>
> TTTTTAGTTTTATTTTATAATAA
>
> TTAAATTATTTAATATATAGTAT

### Demo Run:
> Enter sequence-file name: Demo_NIR(0-5).txt
>
> File contains    6399 sequences.
>
> Number of sequences to process: 6399
> Enforce motif symmetry? y
>
>
> A counts = 71114, %A = 48.32
>
> C counts = 2942, %C =  2.00
>
> G counts = 2843, %G =  1.93
>
> T counts = 70278, %T = 47.75
>
> %AT in subseqs = 96.07
>
> %CG in subseqs =  3.93
>
> Generate score histogram and fitted pdf? y
>
> Output MAT file for fitted params and scoring matrix: T_Output_NIR(0-5)

### Code:
1. Step 1 : Extracts first Subseq_length nucleotides from each read
1. Step 2 : Concatenates each subsequence basecount function expects a single string
1. Step 3 : Compute base-call stats (determine ATGC percentages)
1. Step 4 : Generate base-call stats output
1. Step 5 : Generate profile, positional information matrix, and alignment score
1. Step 6 : Generate sequence logo
1. Step 7 : Fit score distribution to Gaussian along with counts(histogram)
1. Step 8 : Save Gaussian Parameters and scoring matrix to file

### Output: 
The expected output for the demo run is attached as "T_Output_PSSM.jpg", "T_Output_PDF.jpg" and "T_Output_NIR(0-5)"
* Image of PSSM: Sequence logo
  
  ![image](https://user-images.githubusercontent.com/55808380/168644334-6ec7f4fb-74b1-4873-820a-1127ad48d69b.png)


* Image of PDF: Histogram and Gaussian fit 
  
  ![image](https://user-images.githubusercontent.com/55808380/168644509-71c64443-22cf-4c13-9c66-039963a2d123.png)


* Matlab file s.mat: that has the fitted parameters and scoring matrix
