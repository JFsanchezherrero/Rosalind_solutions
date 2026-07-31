## using combinatorics
import math
from Bio import SeqIO
import sys
sequence2check = SeqIO.read(sys.argv[1], format="fasta")

C_count = sequence2check.count("C")
G_count = sequence2check.count("G")
A_count = sequence2check.count("A")
U_count = sequence2check.count("U")

if (A_count == U_count) and (G_count == C_count):
    print(math.factorial(A_count) * math.factorial(G_count))