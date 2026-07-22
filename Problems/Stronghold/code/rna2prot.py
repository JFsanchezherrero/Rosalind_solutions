# Given a file, read it and get information
import sys

with open(sys.argv[1]) as f:
  rna_string = f.read()


from Bio.Seq import Seq
print(Seq(rna_string).translate())

