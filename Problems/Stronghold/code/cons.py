from Bio import SeqIO
import sys

dict_seq = {}
len_seq = {}

##################################################
## read fasta file and get lenght and sequence for each sequence
##################################################
with open(sys.argv[1]) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        ## save sequence & length
        dict_seq[record.id] = str(record.seq)
        len_seq[record.id] = len(record.seq)

## get length and check
from numpy import unique
if all(len_seq.values()):
    val_len = unique(list(len_seq.values()))[0]
    print("\t-All sequences have the same length" + str(val_len))
    
else:
    print("Differences in sequence length")
    print("Finish here...")
    exit()

##################################################
## Create consensus and profile for the alignment
##################################################
cons_seq = ""
profile = []
for i in range(val_len):
    dict_nuc = {"A":0, "C":0, "G":0, "T":0}

    ## count for each column of the alignment 
    ## the amount of each nucleotide
    for [a] in zip(dict_seq.values()):
        dict_nuc[a[i]] += 1

    ## get the profile for each alignment column
    profile.append(list(dict_nuc.values()))
    #print(dict_nuc)

    ## Get most common
    cons_seq += max(dict_nuc, key=lambda k: dict_nuc[k])

## convert it into numpy and transpose
import numpy as np
profile_np = np.array(profile).transpose()

##################################################
## Print output
##################################################
print("")
print(cons_seq)
nucs = ["A", "C", "G", "T"]
for i in range(len(nucs)):
    list_num = np.array2string(profile_np[i]).replace("[", "").replace("]", "").split()
    print(nucs[i] + ": " + " ".join(list_num))