### Aim: 
RoverScan is the Frontend of our Tagmentation project that shows sequence biases and corrects for the same.

It uses lookup table for prediction by linear interpolation. 

### Modules Needed: 
* Matlab
* Computational biology package 

### Files needed in the directory:
* a_Roverscan.m the main script
* ai_LookupTable_CDF.mat For Interpolation CDF table from the trained model
* ai_sore423.mat Scores from PSSM
* FASTA file of intrest here Human Chromosome 1 
* c_FragSizeDist-human.xlsx Fragment size distribution:(From Reva [Fragment size(bp), counts])

### Input : 
Use Hb_Human_ch1_750k-2.5M.fasta as input and follow the demo run below.

### Code:
1. Step 1 : Takes in the FASTA file and give the number of nucleotide and asks the number of base pairs per segment.
1. Step 2 : Provides an option to either truncate or extend the sequence in the multiple of bp/segment.
1. Step 3 : Get the initial coordinates for the fragments from the entire genome.
1. Step 4 : Takes in Fragment size distribution file from REVA incidence file.
1. Step 5 : Compute cleavage probabilities(nu) from interpolated PSSM.
1. Step 6 : Writes the output[Coordinates, Nu] into a text file.
1. Step 7 : Plots a graph of relative cleavage probabilities and Coordinates.

### Run : 
> Enter FASTA file name: b_Human_ch1_750k-2.5M.fasta
>
> File contains 1750001 nucleotides.
>
> Number of base pairs per segment: 50000
>
> Number of base pairs in sequence is not an integer multiple
>
> of segment size. Truncate (T/t) or extend (E/e) sequence? T
>
> New sequence range = 1 - 1750000 bp
>
> Enter file name for fragment size distribution: c_FragSizeDist-human.xlsx
>
> Computing interpolated cleavage probabilities.
>
> Interpolation progress = 3 % complete.
>
> ....
>
> Interpolation progress = 97.1 % complete.
>
> Interpolation of scoring matrix completed.
>
> Elapsed time is x seconds.
>
> nu value for region 1 (: 1 - 50001) = 0.0616
>
> nu value for region 2 (: 50002 - 100000) = 0.0595
>
> .....
>
> nu value for region 34 (: 1650002- 1700000) = 0.0604
>
> nu value for region 35 (: 1700001- 1750000) = 0.0614
>
> Coverage computations completed
>
> File name for output: results_hg


### Output: 
* Text file of Nu_bar values for each segment file.

  [output_hg_chr1.txt](https://github.com/Niha002/Release_Tagmentation/blob/main/4_Roverscan_Frontend/output_hg_chr1.txt)

* Graph depiction of (Relative coverage and coordinates)
  
  [output_hg_chr1.jpg](https://github.com/Niha002/Release_Tagmentation/blob/main/4_Roverscan_Frontend/output_hg_chr1.jpg)
  
  ![image](https://user-images.githubusercontent.com/55808380/168904529-84db364d-c6c1-4213-8a98-e762a8c05b48.png)
