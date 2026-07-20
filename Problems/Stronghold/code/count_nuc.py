# Given a file, read it and count nucleotides
import sys

# input file provided as sys.argv[1] element

## read dna_string information as an example
with open(sys.argv[1]) as f:
  dna_string = f.read()

nucs = ["A", "C", "G", "T"]
counts = [dna_string.count(nuc) for nuc in nucs]
final_string = " ".join(map(str, counts))
print(final_string)
