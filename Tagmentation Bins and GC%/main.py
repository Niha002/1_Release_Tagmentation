from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1 : Get sequences within the range of interest
with open("Demo", "r") as fileInput:  # ------------------input file
    with open("1_Size.txt", "w") as fileOutput:
        # Read each line from sequences
        Lines = fileInput.readlines()
        # Read only [7 before the space & 16 after the space] = 23 Range of interest
        for line in Lines:
            fileOutput.write(line[18:42])  # line so no \n
            fileOutput.write('\n')

# Quality control
# Step 2 : Eliminating the space [needed to calculate GC%]
# Read 1_Size.txt write to 2_Sequence.txt
with open('1_Size.txt', 'r') as fileInput:
    # Eliminating the space
    txt = fileInput.read().replace(' ', '')
with open('2_Sequence.txt', 'w') as fileOutput:
    fileOutput.write(txt)

# Step 2 : Consider only 23bp discard sequences that arent complete
with open('2_Sequence.txt', 'r') as f:
    lines = f.readlines()
    filtered_lines = []
    # Selecting 23bp sequences only
    for line in lines:
        if len(line) >= 23 and line.isupper():
            filtered_lines.append(line)

# Step 3 : Matlab run
# Read 2_Sequence.txt write to 3_Output.txt matlab
with open('7_Demo_unbinned_Matlab.txt', 'w') as fileOutput:
    # Loop through each line in the input file
    for line in filtered_lines:
        fileOutput.write(line)

# write only 23bp sequences out into another file and rearrange the seqID:
with open('3a_Filter_Output.txt', 'w') as f:
    c = 1
    for line in filtered_lines:
        g_seq = 'SeqID_' + str(c)
        # Selecting 30bp sequences only + identifiers
        f.write(">" + g_seq + '\n' + line)
        c += 1

# Step 4 : GC% calculation using Biopython
# Read 3_Output.txt write to 4_GC%.txt
with open('3a_Filter_Output.txt', 'r') as input_fasta:
    seq_objects = SeqIO.parse(input_fasta, 'fasta')
    sequences = [seq for seq in seq_objects]
    no_of_seq = len(sequences)

    # Manage each iteration
    seq_ids = []
    gc_contents = []
    sew = []

    for seq in sequences:
        seq_id = seq.id
        sequence = seq.seq
        sew.append(sequence)  # important to add sequence

        gc_content = GC(sequence)
        gc_content = round(gc_content, 0)  # round off
        # sew = sequence (not storing, list->string, error, no append string)

        # writing to store above in a list
        seq_ids.append(seq_id)
        gc_contents.append(gc_content)

    # Dataframe using pandas headers
    dataframe = pd.DataFrame()
    dataframe['Sequence_ID'] = seq_ids
    dataframe['GC%'] = gc_contents
    dataframe['Sequence'] = sew

    # print(dataframe)

    # Write results in 4_GC%.txt with headers as printed above
    dataframe.to_csv("4_GC%.txt", sep='\t', mode='w')

# Step 5 : Statistics from 4_GC%
with open('4_GC%.txt', 'r') as input_GC:
    describe = dataframe[["GC%", "Sequence_ID"]].describe()
    print(describe)
    with open('5_Statistics_4_GC%.txt', 'w') as f:
        f.write(str(describe))

# Step 6 : Creating bins for 4_GC% in increment of 5
    a = pd.cut(dataframe['GC%'], bins=np.linspace(0, 100, 21)).value_counts()  # via count ranking descending
    b = pd.cut(dataframe['GC%'], include_lowest = True, bins = np.linspace(0, 100, 21)).value_counts().sort_index(ascending=True)
    print(b)  # [include (not include

    b.to_csv("6_Bin_Counts.txt", sep='\t', mode='w')

# Step 7 : Creating text bins for 4_GC% in increment of 5
with open("4_GC%.txt", "r") as fileInput:
    pr = dataframe['GC%']
    q = dataframe['Sequence']

    # Creating a dictionary with keys as ranges
    dict_of_seq = {}
    Range = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50',
             '50-55', '55-60', '60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100']
    for x in Range:
        dict_of_seq[x] = []

    # Assigning keys to respective ranges
    for index, item in enumerate(pr):
        if item > 95:
            dict_of_seq['95-100'].append(str(q[index]))

        elif item <= 95 and item > 90:
            dict_of_seq['90-95'].append(str(q[index]))

        elif item <= 90 and item > 85:
            dict_of_seq['85-90'].append(str(q[index]))

        elif item <= 85 and item > 80:
            dict_of_seq['80-85'].append(str(q[index]))

        elif item <= 80 and item > 75:
            dict_of_seq['75-80'].append(str(q[index]))

        elif item <= 75 and item > 70:
            dict_of_seq['70-75'].append(str(q[index]))

        elif item <= 70 and item > 65:
            dict_of_seq['65-70'].append(str(q[index]))

        elif item <= 65 and item > 60:
            dict_of_seq['60-65'].append(str(q[index]))

        elif item <= 60 and item > 55:
            dict_of_seq['55-60'].append(str(q[index]))

        elif item <= 55 and item > 50:
            dict_of_seq['50-55'].append(str(q[index]))

        elif item <= 50 and item > 45:
            dict_of_seq['45-50'].append(str(q[index]))

        elif item <= 45 and item > 40:
            dict_of_seq['40-45'].append(str(q[index]))

        elif item <= 40 and item > 35:
            dict_of_seq['35-40'].append(str(q[index]))

        elif item <= 35 and item > 30:
            dict_of_seq['30-35'].append(str(q[index]))

        elif item <= 30 and item > 25:
            dict_of_seq['25-30'].append(str(q[index]))

        elif item <= 25 and item > 20:
            dict_of_seq['20-25'].append(str(q[index]))

        elif item <= 20 and item > 15:
            dict_of_seq['15-20'].append(str(q[index]))

        elif item <= 15 and item > 10:
            dict_of_seq['10-15'].append(str(q[index]))

        elif item <= 10 and item > 5:
            dict_of_seq['5-10'].append(str(q[index]))

        elif item <= 5 and item >= 0:
            dict_of_seq['0-5'].append(str(q[index]))

    for Range in dict_of_seq:
        with open("Z_Demo_R1_Range " + Range + ".txt", "w") as fileOutput:
            for i in range(0, len(dict_of_seq[Range])):
                fileOutput.write('>Demo_R1_Seq_' + str(i+1) + '\n' + dict_of_seq[Range][i] + '\n')

    for Range in dict_of_seq:
        with open("ZNI_Demo_R1_Range " + Range + ".txt", "w") as fileOutput:
            for i in range(0, len(dict_of_seq[Range])):
                fileOutput.write(dict_of_seq[Range][i]+ '\n')