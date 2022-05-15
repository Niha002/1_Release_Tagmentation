### Aim: 
Makes a sequence logo to see sequence biases in Tn5 region activity and PDF for each bins, where each sequence is 23bp(7:16).

Training the input data from the whole pan genome ensemble from step 2c and 2d.

Run the whole un-binned genome(pan-genome ensemble) first and save it as T0_final.mat file. Then run it against binned genome (increments of 5)

Similar to the previous run 3a but against the PSSM profile
     
### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* A,T,G,C image file .png
* T0_func_seqlogo.m
* Binned files from step 2c/2d pan genome ensemble 
* T0_final.mat (make sure its loaded in workspace before the run)

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

### Output: 
The expected output is 

* Image of PDF: Histogram and gaussian fit 

  <img width="392" alt="image" src="https://user-images.githubusercontent.com/55808380/168490804-9ba766a6-d349-43d1-a18a-f142d8bd534e.png">

* Matlab file s.mat: that has the PSSM profile
