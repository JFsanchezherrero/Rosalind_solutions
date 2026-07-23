
# input file provided as sys.argv[1] element
import sys

## read dna_string information as two separate string
with open(sys.argv[1]) as f:
  information2use = f.read().strip()

## Data in file
print("## Data available in file")
print(information2use)
print()
info_list = information2use.split("\n")
string2search = info_list[0] + "[ORGN] AND (\"" + info_list[1] + "\"[PDAT]:\"" + info_list[2] + "\"[PDAT])"

print("## String to search in NCBI Genbank nucleotide")
print(string2search)
print()
# load Biopython module Entrez
from Bio import Entrez
Entrez.email = 'JoseFrancisco.Sanchez@uab.cat'

#Connect GenBank:
handle = Entrez.esearch(db="nucleotide", term=string2search)
## provide the term of interest using appropiate tags [ORGN], [TITL]

# Save results (XML format as default)
# and close connection
results = Entrez.read(handle)
handle.close()
print()
print("Number of results: " + str(results['Count']))
