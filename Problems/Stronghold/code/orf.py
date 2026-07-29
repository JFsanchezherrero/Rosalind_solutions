from Bio import SeqIO
from Bio.Seq import Seq
import sys
import regex as re

re_str = '(M[^*]*)\\*'

hits_append=[]
translate_seq_list=[]

debug_flag=0

input_seq = SeqIO.read(sys.argv[1], format="fasta")
if debug_flag:
    print(input_seq)
    print(input_seq.reverse_complement().seq)

total_len = len(input_seq)
seqs2check = [input_seq, input_seq.reverse_complement()]
for i in [0,1,2]:
    for s in seqs2check:
        translate_seq = s[i:total_len].translate().seq
        if debug_flag:
            print("--------------------")
            print(translate_seq)

        ## get sequences
        translate_seq_list.append(str(translate_seq))

        ## get ORFs
        hits_append.append(re.findall(pattern=re_str, 
                                    string=str(translate_seq),
                                    overlapped=True))

import itertools
hits_unlist = list(itertools.chain.from_iterable(hits_append))
hits_unlist = list(set(hits_unlist))

print("\n".join(hits_unlist))
