# Permutation combinations for 23bp to score them

# Since its format of palindrome (1:11) N (12:23)
# Workflow
# 1. Generate permutations of first 1st 11 bp -> File 1
# 2. Take File 1 and reverse it and print mirror sequence in File 1 [File 1 = AT, File 2 = ATTA]
# 3. Insert A, T G, C in between at position 12 -> 4 files
# 4. Combine all files

# 1. Function for permutation
def all_seq(n, curr, e, ways):
    """All possible sequences of size n given elements e.
    ARGS
        n: size of sequence
        curr: a list used for constructing sequences
        e: the list of possible elements (could have been a global list instead)
        ways: the final list of sequences
    """
    if len(curr) == n:
        ways.append(''.join(curr))
        return
    for element in e:
        all_seq(n, list(curr) + [element], e, ways)
#------------------------------------------ 1. Generate permuatations ------------------------------------------
perms = []
all_seq(11, [], ['A', 'C', 'T', 'G'], perms) #-------------------------------------------(*)

# 1. Convert lists of output into file 1
# print(perms) # list
with open('p1.txt', 'w') as fileOutput:
    for seq in perms:
        fileOutput.write(str(seq)),
        fileOutput.write('\n')
# Eliminate white spaces
output=""
with open('p1.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("p1b_nospace.txt","w")
f.write(output)

#------------------------------------------ 2. Function to reverse the sequence---------------------------------
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
with open('p1.txt', 'r') as fileInput:
    with open("p2.txt", "w") as fileOutput2:
        # Read each line from sequences
        Lines = fileInput.readlines()
        for line in Lines:
            fileOutput2.write(reverse(line)+line),
# Eliminate white spaces
output1=""
with open('p2.txt') as f:
    for line in f:
        if not line.isspace():
            output1+=line
f = open("p2b_nospace.txt","w")
f.write(output1)

# ************************************ Save the file as demo delete the extra line below
# ------------------------------------------3. Insert A, T G, C in between at position 12 ---------------------
# ************************************ A ************************************
with open('demo.txt', 'r') as fileInput:
    sequence1 = fileInput.read()
    tem = sequence1.split('\n')
    print(sequence1)
    with open("d1.txt", "w") as fileOutput:
        for x in tem:
            #insert = insertChar(sequence1,2, '-')
            x = x[:11] + "A" + x[11:] +'\n'
            fileOutput.write(x)
# ************************************ T ************************************
with open('demo.txt', 'r') as fileInput:
    sequence1 = fileInput.read()
    tem = sequence1.split('\n')
    print(sequence1)
    with open("d2.txt", "w") as fileOutput:
        for x in tem:
            #insert = insertChar(sequence1,2, '-')
            x = x[:11] + "T" + x[:11] +'\n'
            fileOutput.write(x)
# ************************************ G ************************************
with open('demo.txt', 'r') as fileInput:
    sequence1 = fileInput.read()
    tem = sequence1.split('\n')
    print(sequence1)
    with open("d3.txt", "w") as fileOutput3:
        for x in tem:
            #insert = insertChar(sequence1,2, '-')
            x = x[:11] + "G" + x[:11] +'\n'
            fileOutput3.write(x)
# ************************************ C ************************************
with open('demo.txt', 'r') as fileInput:
    sequence1 = fileInput.read()
    tem = sequence1.split('\n')
    print(sequence1)
    with open("d4.txt", "w") as fileOutput3:
        for x in tem:
            #insert = insertChar(sequence1,2, '-')
            x = x[:11] + "C" + x[:11] +'\n'
            fileOutput3.write(x)

# ------------------------------------------4. Combine all files ------------------------------------------
import shutil
# ---------------------------PART A: Bin Files ---------------------------
# Merging sequences below each other
with open('Combine.txt', 'w') as wfd:
    for f in ['d1.txt', 'd2.txt', 'd3.txt', 'd4.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('Combine.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("Combine.txt","w")
f.write(output)
