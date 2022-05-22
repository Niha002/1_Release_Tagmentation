# Splits a huge file having all chromosome fasta to single files fastas sequentially
# To extract Chr1 from No_alts file

from Bio import SeqIO

"""
    Returns lists of length batch_size.
    
    This can be used on any iterator, for example to batch up
    SeqRecord objects from Bio.SeqIO.parse(...), or to batch
    Alignment objects from Bio.AlignIO.parse(...), or simply
    lines from a file handle.
    This is a generator function, and it returns lists of the
    entries from the supplied iterator.  Each list will have
    batch_size entries, although the final list may be shorter.
    """

def batch_iterator(iterator, batch_size) :
    
    entry = True #Make sure we loop once
    while entry :
        batch = []
        while len(batch) < batch_size :
            try :
                entry = next(iterator)
            except StopIteration :
                entry = None
            if entry is None :
                #End of file
                break
            batch.append(entry)
        if batch :
            yield batch


infile = input('Which .fasta file would you like to open? ')
record_iter = SeqIO.parse(open(infile), "fasta")
for i, batch in enumerate(batch_iterator(record_iter, 1)) :
    outfile = "c:\python32\myfiles\%i.fasta" % (i+1)
    handle = open(outfile, "w")
    count = SeqIO.write(batch, handle, "fasta")
    handle.close()
    print ("Wrote %i records to %s" % (count, outfile)) 

# Find the no. of nucleotides in the file (not accurate yet)
#open file in read mode
file = open("chr1.fasta", "r")
#read the content of file
data = file.read()
#get the length of the data
number_of_characters = len(data)
print('Number of characters in text file :', number_of_characters)
