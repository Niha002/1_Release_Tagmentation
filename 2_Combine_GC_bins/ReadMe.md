# Combine Bins

### Aim: 
To combine permutation and combination of GC Bins(files or boxes of classification) for analysis.

All the scripts in this directory use the similar code that achieves the following:
* Reads from multiple files 
* combines the data(sequences) within each file  
* Eliminates white-space
* Outputs the data(sequences) one below the other

### Modules Needed: 
* shutil

### Input: 
* We need file from Script folder 1: [Tagmentation Bins and GC%](https://github.com/Niha002/Release_Tagmentation/tree/main/1_Tagmentation%20Bins%20and%20GC%25)
* Have those file in the same folder as the .py script
* Modify the code to include the files in the array structure based on the script used.

  Based on the editor use to Ctrl find and replace option for convenience.
  > Ex. for f in ['a.txt', 'b.txt', 'c.txt']:

# Scripts
1. Same organism R1 + R2: 
2. All R1 reads or All R2 reads: 
3. Combine all sequences in GC bins
4. Combine all sequences unbinned

# Summary
Example 3 organism x, y, z

Where r1, r2 two reads for the same genome

>           r1_x    r2_x      r1_y     r2_y       r1_z    r2_z          : Data looks like
>           r1_x              r1_y                r1_z                  : All R1 reads 
>                   r2_x               r2_y               r2_z          : All R2 reads
>                x                  y                  z                : Same organism R1 + R2
>                                  all bins                             : Combine all sequences binned
>                                  all unbinned                         : Combine all sequences unbinned             


# 1. Same organism R1 + R2: 
Here in our case from Script folder 1: [Tagmentation Bins and GC%](https://github.com/Niha002/Release_Tagmentation/tree/main/1_Tagmentation%20Bins%20and%20GC%25) we would get:

For a genome x
* x_R1 files - 20 bins
  
  x_R2 files - 20 bins

We want to combine them to get x_same_organism 20 respective merged bins 

> Combine syntax
> * x_R1(20) + x_R2(20) = x_same_organism(20) 

# 2. All R1 reads or All R2 reads: 
Here in our case from Script folder 1: [Tagmentation Bins and GC%](https://github.com/Niha002/Release_Tagmentation/tree/main/1_Tagmentation%20Bins%20and%20GC%25) we would get:

For a genome x, y, z
* x_R1 files - 20 bins 

  y_R1 files - 20 bins

  z_R1 files - 20 bins 

* x_R2 files - 20 bins 

  y_R2 files - 20 bins 

  z_R2 files - 20 bins 

We want to combine each set to get R1_different_organism and R2_different_organism to get 20 bins for each case
> Combine syntax
> * x_R1(20) + y_R1(20) + z_R1(20) = x_y_z_R1(20)
> * x_R2(20) + y_R2(20) + z_R2(20) = x_y_z_R2(20)

# 3. Combine all sequences in GC bins
Here in our case from Script folder 1: [Tagmentation Bins and GC%](https://github.com/Niha002/Release_Tagmentation/tree/main/1_Tagmentation%20Bins%20and%20GC%25) we would get:

For a genome x, y, z
* x_R1 & x_R2 files - 40 bins (20 each)

  y_R1 & y_R2 files - 40 bins (20 each)

  z_R1 & z_R2 files - 40 bins (20 each)

We want to combine to get all sequences in 20 bins
> Combine syntax
> * x_R1(20) + x_R2(20) + y_R1(20) +  y_R2(20) + z_R1(20) + z_R2(20) = x_y_z_(20)
> * x_R1 & x_R2(40) + y_R1 & y_R2(40) + z_R1 & z_R2(40) = x_y_z_(20)

# 4. Combine all sequences unbinned
We want one file will all the sequences
Here in our case from script 3 '_Combine all sequences in GC bins_' above we would get:

For a genome x, y, z
* x_y_z_(20) - 20 bins 

We want to combine x_y_z_(20) to get all sequences in one bin
> Combine syntax
> * x_y_z_(20) - 1 file
