
# Given a file, read it and get information
import sys

from Bio.SeqUtils import gc_fraction
from Bio import SeqIO

dict_GC = {}
with open(sys.argv[1]) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        dict_GC[record.id] = [gc_fraction(record), record.seq]

res = max(dict_GC, key=lambda k: dict_GC[k][0])

print(res + "\n" + str(100*dict_GC[res][0]))
