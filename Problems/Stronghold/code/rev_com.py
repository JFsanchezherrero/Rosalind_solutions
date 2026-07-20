# Given a file, read it and count nucleotides
import sys

# input file provided as sys.argv[1] element

## read dna_string information as an example
with open(sys.argv[1]) as f:
  dna_string = f.read()

from Bio.Seq import Seq
print(str(Seq(dna_string).reverse_complement()))