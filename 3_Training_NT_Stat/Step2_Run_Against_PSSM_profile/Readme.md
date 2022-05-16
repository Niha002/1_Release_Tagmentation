### Aim: 
Makes a sequence logo to see sequence biases in Tn5 region activity and PDF for each bins, where each sequence is 23bp(7:16).

Training the input data from the whole pan genome ensemble from step 2c and 2d.

Run the whole un-binned genome(pan-genome ensemble) first and save it as T0_final.mat file. Then run it against binned genome (increments of 5)

Similar to the previous run 3a but against the PSSM profile of the pan-genome ensemble.
     
### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* Binned files from step 2c/2d pan genome ensemble 
* T0_final.mat (make sure its loaded in workspace before the run)

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
> Output MAT file for fitted params and scoring matrix: T0_Output_NIR(0-5)_against

### Code:
1. Step 1 : Extracts first Subseq_length nucleotides from each read
1. Step 2 : Concatenates each subsequence basecount function expects a single string
1. Step 3 : Compute base-call stats (determine ATGC percentages)
1. Step 4 : Generate base-call stats output
1. Step 5 : Extracts PSSM from T0_final.mat file
1. Step 6 : Fit score distribution to Gaussian along with counts(histogram)
1. Step 7 : Save Gaussian Parameters and scoring matrix to file

### Output: 
The expected output for the demo run is attached as [T_Output_PDF_against.jpg](https://github.com/Niha002/Release_Tagmentation/blob/main/3_Training_NT_Stat/Step2_Run_Against_PSSM_profile/T_Output_PDF_against.jpg) and [T_Output_NIR(0-5)_against.mat](https://github.com/Niha002/Release_Tagmentation/blob/main/3_Training_NT_Stat/Step2_Run_Against_PSSM_profile/T_Output_NIR(0-5)_against.mat)
* Image of PDF: Histogram and Gaussian fit 
  
 ![image](https://user-images.githubusercontent.com/55808380/168662482-f55bccb3-2685-442a-b96e-8728596e130e.png)

* Matlab file [T_Output_NIR(0-5)_against.mat](https://github.com/Niha002/Release_Tagmentation/blob/main/3_Training_NT_Stat/Step2_Run_Against_PSSM_profile/T_Output_NIR(0-5)_against.mat) (s.mat) that has the Gaussian Parameters and scoring matrix.
