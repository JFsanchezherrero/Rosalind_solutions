from Bio import SeqIO
import sys

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

##################################################
# Generate all substrings using list comprehension
##################################################
substrings_all = [shortest_seq[i:j] for i in range(len(shortest_seq)) for j in range(i+1, len(shortest_seq)+1)]
## return only longer or equal to 2
substrings = [s for s in substrings_all if len(s) > 1]
## sort from longest-shortest
substrings = sorted(substrings, key=len)[::-1]


##################################################
## get all matches for all sequences
##################################################
## get remaining sequences to index
seqs2test =  list(dict_seq.keys() - [shortest_seq_id])
## get sequences to test
sub_substrings = {}
for s2test in seqs2test:
    list_tmp = []
    for s in substrings:
        #print("sub")
        #print(s)
        if (dict_seq[s2test].find(s)>0):
            list_tmp.append(s)

    sub_substrings[s2test]=list_tmp


## count, sort and arrange
from collections import Counter
counter = Counter(item for values in sub_substrings.values() for item in set(values))
print(counter)
common = [item for item, count in counter.items() if count >= 2]
common_longest = sorted(common, key=len)[::-1]

##################################################
## Print output
##################################################
print(common_longest)