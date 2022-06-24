from Bio import SeqIO

% All files in same directory to convert to Uppercase as Roverscan in case sensitive
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 'X', 'Y'];
for x in numlist:
    records = (rec.upper() for rec in SeqIO.parse("Chr_"+str(x)+".fasta", "fasta"))
    count = SeqIO.write(records, "U_Chr_"+str(x)+".fasta", "fasta")
    print("Converted %i records to upper case" %count)
