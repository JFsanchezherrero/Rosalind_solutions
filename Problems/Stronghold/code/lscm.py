from Bio import SeqIO
import sys

from progress.spinner import Spinner

spinner = Spinner('Working...')
    
##################################################
## get sequences
##################################################
dict_seq = {}
len_seq = {}
with open(sys.argv[1]) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        ## save sequence & length
        dict_seq[record.id] = str(record.seq)
        len_seq[record.id] = len(record.seq)

## get shortest sequence
shortest_seq_id = min(len_seq, key=lambda k: len_seq[k])
shortest_seq = dict_seq[shortest_seq_id]

from collections import defaultdict
dict_motif = defaultdict(int)

min_lentgh_motif = 100

## get remaining sequences to index
seqs2test =  list(dict_seq.keys() - [shortest_seq_id])

## apply parallel threads
for i in range(len(shortest_seq)):

    ## let the spinner sping
    spinner.next()

    for j in range(i+1, len(shortest_seq)+1):
        substrings_str = shortest_seq[i:j]
        ## debug
        #print(substrings_str)
        #print(len(substrings_str))
        if (len(substrings_str) < min_lentgh_motif):
            #print("Very small")
            continue
        
        ## debug
        #print("i - j:" + str(i) + " - " + str(j))
        #print(substrings_str)
               
        ## get all matches for all sequences
        for s2test in seqs2test:
            #print(s2test)
            if (dict_seq[s2test].find(substrings_str)>0):
                dict_motif[substrings_str] += 1

print("\n+ Done")

## filter motifs found in all sequences
dict_motif_all = {k: v for k, v in dict_motif.items() if v==99}

## get longest
res = max(dict_motif_all.keys(), key=lambda k: len(k))
print("+ Longest motif is:")
print(res)