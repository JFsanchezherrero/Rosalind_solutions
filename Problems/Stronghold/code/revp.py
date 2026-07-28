from Bio import SeqIO 
from Bio.Seq import Seq
import sys

seq2check = SeqIO.read(sys.argv[1], format="fasta")

debug_flag = 1
palindromic_hits = {}
min_len_pal=4
max_len_pal=12
for i in range(len(seq2check)):
    for j in range(min_len_pal, max_len_pal+1):

        end_bp = i+j

        ## skip if longer than sequence
        if (end_bp > len(seq2check)):
            break

        sub1 = str(seq2check.seq[i:end_bp])
        sub2 = str(Seq(sub1).reverse_complement())

        ## testing debug
        if debug_flag == 2:
            print("Position: " + str(i))
            print("Subset: " + str(i) + ":" + str(end_bp))
            print(sub1)

        ## check if sequences match    
        if (sub1==sub2):
            ## keep track of results
            palindromic_hits["pos_" + str(i) + "_" + str(j)] = [i+1, end_bp+1, j, sub1, sub2]

            if debug_flag > 0:
                print("#######################")
                print("Match!")
                print("Subset: " + str(i) + ":" + str(end_bp))
                print(sub1)
                print("|"*len(sub1))
                print(Seq(sub1).complement())
                print("#######################")
                print()

if debug_flag > 0:
    print(palindromic_hits)

print("\n".join([str(v[0]) + " " + str(v[2]) for k,v in palindromic_hits.items()]))