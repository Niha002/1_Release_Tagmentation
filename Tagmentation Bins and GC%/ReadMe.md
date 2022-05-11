Aim: Gather the region of Tn5 enzyme activity 23bp 
     This 23bp can be divide into
	 - 7bp overhang reconstructed from reference genome
	 - 16bp tagmented sequence read
     Compiles the 23bp reads from the raw data 

Modules Needed: BioPython, Numpy, Pandas, matplotlib

Input: One file with reads of the following format
	TCACCCCGCAACTGGGCATGGAGTT TCCCCAGGAGGTCGACTTCAAGGCGGTCTACGCCAGTTGCTCGGTGTTCTGCGAGCAGGTGCACAGCCCGGAACAGGCGCGCCGGGTGCTGGCCCTGGCCT
	TTTCAAGGAAGCCTATGCACAGTAC GTCGAGGGTGGCTGGAACGGTGTCGCCAGCGATCCCGCGTACGGCGGCCAGGGCCTGCCGCACTCGCTGGGTCTGCTGCTCAGCGAGATGATCGGCTCCAC
				.
				.
				.
	TGTTACTGCCTGACGGACGCGCCGG GTCGAGGGTGGCTGGAACGGTGTCGCCAGCGATCCCGCGTACGGCGGCCAGGGCCTGCCGCACTCGCTGGGTCTGCTGCTCAGCGAGATGATCGGCTCCAC
	TCACCCCGCAACTGGGCATGGAGTT TCCCCAGGAGGTCGACTTCAAGGCGGTCTACGCCAGTTGCTCGGTGTTCTGCGAGCAGGTGCACAGCCCGGAACAGGCGCGCCGGGTGCTGGCCCTGGCCT

Before Run: Line 9 in the main.py file 
    	    Place the name of your dat file within "" as shown
		        with open("1_Data_SRR8526281_R1.ext.dat", "r") as fileInput:

Code:
	Step 1 : Get sequences within the range of interest
	Step 2 : Quality control Consider only 23bp discard sequences that arent complete
	Step 3 : Matlab run no identifiers and another set with unique identifiers[genome_read_number]
	Step 4 : GC% calculation using Biopython
	Step 5 : basic statistics for the GC% calculation
	Step 6 : Creating bins for GC% in increments of 5

Output: Each of the steps will have its own txt file and with its output for the demo file given here.
            Step 1 : 1_Size.txt
                        ATAGGCT GTCTTGTCTTGCTTGC
                        CGCGGCA CGCCGGCACCGCCGTG
                        CGCAACA GAGCCAGTGCGAAAGC
                        TGGTATC CGCCAGGGCCACCCCG
	        Step 2 : 2_Sequence.txt
	                    ATAGGCTGTCTTGTCTTGCTTGC
                        CGCGGCACGCCGGCACCGCCGTG
                        CGCAACAGAGCCAGTGCGAAAGC
                        TGGTATCCGCCAGGGCCACCCCG
	        Step 3 : 3a_Filter_Output.txt
	                    >SeqID_1
                        ATAGGCTGTCTTGTCTTGCTTGC
                        >SeqID_2
                        CGCGGCACGCCGGCACCGCCGTG
                        >SeqID_3
                        CGCAACAGAGCCAGTGCGAAAGC
                        >SeqID_4
                        TGGTATCCGCCAGGGCCACCCCG
                     7_Demo_unbinned_Matlab.txt
                        ATAGGCTGTCTTGTCTTGCTTGC
                        CGCGGCACGCCGGCACCGCCGTG
                        CGCAACAGAGCCAGTGCGAAAGC
                        TGGTATCCGCCAGGGCCACCCCG
	        Step 4 : 4_GC%.txt
                            Sequence_ID	GC%	    Sequence
                        0	SeqID_1	    48.0	ATAGGCTGTCTTGTCTTGCTTGC
                        1	SeqID_2	    87.0	CGCGGCACGCCGGCACCGCCGTG
                        2	SeqID_3	    61.0	CGCAACAGAGCCAGTGCGAAAGC
                        3	SeqID_4	    74.0	TGGTATCCGCCAGGGCCACCCCG
                        4	SeqID_5	    61.0	GCAAGGTGTGCGTGAGCGAGAAG
	        Step 5 : 5_Statistics_4_GC%.txt
                        count  46.000000
                        mean   63.130435
                        std     8.963156
                        min    48.000000
                        25%    57.000000
                        50%    61.000000
                        75%    70.000000
                        max    87.000000
	                 6_Bin_Counts.txt
                        GC%             Count
                        (-0.001, 5.0]	0
                        (5.0, 10.0]	0
                        (10.0, 15.0]	0
                        (15.0, 20.0]	0
                        (20.0, 25.0]	0
                        (25.0, 30.0]	0
                        (30.0, 35.0]	0
                        (35.0, 40.0]	0
                        (40.0, 45.0]	0
                        (45.0, 50.0]	1
                        (50.0, 55.0]	7
                        (55.0, 60.0]	9
                        (60.0, 65.0]	16
                        (65.0, 70.0]	4
                        (70.0, 75.0]	4
                        (75.0, 80.0]	4
                        (80.0, 85.0]	0
                        (85.0, 90.0]	1
                        (90.0, 95.0]	0
                        (95.0, 100.0]	0
            Step 6 : 20 files with identifiers
                        Z_Demo_R1_Range 0-5.txt
                        Each file will look like below
                            Z_Demo_R1_Range 65-70.txt
                                >Demo_R1_Seq_1
                                CGGCGAAGGCGTGCATGGTACGG
                                >Demo_R1_Seq_2
                                AGCGCCGGGGTCAGCTTGGGGAA
                                >Demo_R1_Seq_3
                                AACGCCAGGCGCGGGAGAGTGAC
                                >Demo_R1_Seq_4
                                GCGGCCTGCCTACACGCGTTCTG
                    20 files without identifiers
                        Z_Demo_R1_Range 0-5.txt
                            Each file will look like below
                                Z_Demo_R1_Range 65-70.txt
                                    CGGCGAAGGCGTGCATGGTACGG
                                    AGCGCCGGGGTCAGCTTGGGGAA
                                    AACGCCAGGCGCGGGAGAGTGAC
                                    GCGGCCTGCCTACACGCGTTCTG
